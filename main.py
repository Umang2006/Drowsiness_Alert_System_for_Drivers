import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates as denormalize_coordinates

# ----------------- Mediapipe FaceMesh Initialization -----------------
def get_mediapipe_app(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
):
    """
    Initialize and return Mediapipe FaceMesh Solution object.
    """
    face_mesh = mp.solutions.face_mesh.FaceMesh(
        max_num_faces=max_num_faces,
        refine_landmarks=refine_landmarks,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )
    return face_mesh

# ----------------- Utility Functions -----------------
def distance(point_1, point_2):
    """
    Calculate Euclidean (L2) distance between two points.
    """
    return sum([(i - j) ** 2 for i, j in zip(point_1, point_2)]) ** 0.5

def get_ear(landmarks, refer_idxs, frame_width, frame_height):
    """
    Calculate Eye Aspect Ratio (EAR) for one eye.
    Returns EAR and the eye landmark coordinates.
    """
    try:
        coords_points = []
        for i in refer_idxs:
            lm = landmarks[i]
            coord = denormalize_coordinates(lm.x, lm.y, frame_width, frame_height)
            coords_points.append(coord)
        # Calculate distances between key points
        P2_P6 = distance(coords_points[1], coords_points[5])
        P3_P5 = distance(coords_points[2], coords_points[4])
        P1_P4 = distance(coords_points[0], coords_points[3])
        ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
    except:
        ear = 0.0
        coords_points = None
    return ear, coords_points

def calculate_avg_ear(landmarks, left_eye_idxs, right_eye_idxs, image_w, image_h):
    """
    Calculate average EAR for both eyes.
    """
    left_ear, left_lm_coordinates = get_ear(landmarks, left_eye_idxs, image_w, image_h)
    right_ear, right_lm_coordinates = get_ear(landmarks, right_eye_idxs, image_w, image_h)
    Avg_EAR = (left_ear + right_ear) / 2.0
    return Avg_EAR, (left_lm_coordinates, right_lm_coordinates)

def plot_eye_landmarks(frame, left_lm_coordinates, right_lm_coordinates, color):
    """
    Draw circles for eye landmarks on the frame.
    """
    for lm_coordinates in [left_lm_coordinates, right_lm_coordinates]:
        if lm_coordinates:
            for coord in lm_coordinates:
                cv2.circle(frame, coord, 2, color, -1)
    frame = cv2.flip(frame, 1)
    return frame

def plot_text(image, text, origin, color, font=cv2.FONT_HERSHEY_SIMPLEX, fntScale=0.8, thickness=2):
    """
    Overlay text on the frame.
    """
    return cv2.putText(image, text, origin, font, fntScale, color, thickness)

# ----------------- Main Handler Class -----------------
class VideoFrameHandler:
    def __init__(self):
        """
        Initialize constants, Mediapipe FaceMesh, and state trackers.
        """
        # Landmark indices for left and right eyes (Mediapipe FaceMesh)
        self.eye_idxs = {
            "left": [362, 385, 387, 263, 373, 380],
            "right": [33, 160, 158, 133, 153, 144],
        }
        # Colors for visual feedback
        self.RED = (0, 0, 255)    # Drowsy
        self.GREEN = (0, 255, 0)  # Awake
        # Initialize FaceMesh
        self.facemesh_model = get_mediapipe_app()
        # State tracking for drowsiness logic
        self.state_tracker = {
            "start_time": time.perf_counter(),
            "DROWSY_TIME": 0.0,
            "COLOR": self.GREEN,
            "play_alarm": False,
        }
        self.EAR_txt_pos = (10, 30)

    def enhance_image(self, frame):
        """
        Enhance the input frame for better detection in low-light conditions.
        Steps:
        - Convert to grayscale
        - Apply histogram equalization for contrast
        - Convert back to BGR
        - Adjust brightness and contrast
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        enhanced_frame = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
        # Adjust brightness and contrast (alpha: contrast, beta: brightness)
        alpha = 1.2  # Contrast control (1.0-3.0)
        beta = 10    # Brightness control (0-100)
        enhanced_frame = cv2.convertScaleAbs(enhanced_frame, alpha=alpha, beta=beta)
        return enhanced_frame

    def process(self, frame: np.array, thresholds: dict):
        """
        Main drowsiness detection logic.
        - Enhances the frame for low-light
        - Runs FaceMesh and computes EAR
        - Tracks drowsy time and triggers alarm if needed
        Returns:
            frame (np.array): Processed frame for display
            play_alarm (bool): Whether to trigger alarm
        """
        # Enhance image for low-light conditions
        frame = self.enhance_image(frame)
        frame.flags.writeable = False
        frame_h, frame_w, _ = frame.shape
        DROWSY_TIME_txt_pos = (10, int(frame_h // 2 * 1.7))
        ALM_txt_pos = (10, int(frame_h // 2 * 1.85))

        results = self.facemesh_model.process(frame)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            EAR, coordinates = calculate_avg_ear(landmarks, self.eye_idxs["left"], self.eye_idxs["right"], frame_w, frame_h)
            frame = plot_eye_landmarks(frame, coordinates[0], coordinates[1], self.state_tracker["COLOR"])
            if EAR < thresholds["EAR_THRESH"]:
                # If EAR below threshold, accumulate drowsy time
                end_time = time.perf_counter()
                self.state_tracker["DROWSY_TIME"] += end_time - self.state_tracker["start_time"]
                self.state_tracker["start_time"] = end_time
                self.state_tracker["COLOR"] = self.RED
                if self.state_tracker["DROWSY_TIME"] >= thresholds["WAIT_TIME"]:
                    self.state_tracker["play_alarm"] = True
                    plot_text(frame, "WAKE UP! WAKE UP", ALM_txt_pos, self.state_tracker["COLOR"])
            else:
                # Reset drowsy time if EAR above threshold
                self.state_tracker["start_time"] = time.perf_counter()
                self.state_tracker["DROWSY_TIME"] = 0.0
                self.state_tracker["COLOR"] = self.GREEN
                self.state_tracker["play_alarm"] = False
            # Overlay EAR and drowsy time
            EAR_txt = f"EAR: {round(EAR, 2)}"
            DROWSY_TIME_txt = f"DROWSY: {round(self.state_tracker['DROWSY_TIME'], 3)} Secs"
            plot_text(frame, EAR_txt, self.EAR_txt_pos, self.state_tracker["COLOR"])
            plot_text(frame, DROWSY_TIME_txt, DROWSY_TIME_txt_pos, self.state_tracker["COLOR"])
        else:
            # No face detected: reset state
            self.state_tracker["start_time"] = time.perf_counter()
            self.state_tracker["DROWSY_TIME"] = 0.0
            self.state_tracker["COLOR"] = self.GREEN
            self.state_tracker["play_alarm"] = False
            frame = cv2.flip(frame, 1)
        return frame, self.state_tracker["play_alarm"]
