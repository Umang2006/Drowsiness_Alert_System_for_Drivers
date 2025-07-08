# DrowSee: Driver Drowsiness Detection System
## Overview
**DrowSee** is a real-time driver drowsiness detection system designed to enhance road safety by identifying early signs of driver fatigue. The project leverages computer vision techniques to monitor behavioral cues, such as eye movements, and provides timely alerts to prevent potential accidents. This repository contains the code and resources for the implementation using Python, OpenCV, and Mediapipe.

## Motivation
Driver fatigue is a significant contributor to road accidents worldwide, often resulting in impaired reaction times and poor decision-making. Many drivers underestimate the impact of drowsiness, making proactive detection systems crucial for safety. DrowSee aims to address this challenge by offering a distraction-free, real-time monitoring solution that can be integrated seamlessly into the driving experience.

## Project Objectives
- **Accurately detect signs of driver drowsiness** using facial landmark analysis and Eye Aspect Ratio (EAR) computation.
- **Provide real-time alerts** to drivers when drowsiness is detected, enabling timely corrective action.
- **Design a modular and adaptable system** that can be further extended for embedded or in-vehicle deployment.
- **Promote road safety** by reducing the risk of accidents caused by driver fatigue.

## Features
- Real-time video processing from a standard webcam.
- Facial landmark detection using Mediapipe for robust eye tracking.
- Calculation of Eye Aspect Ratio (EAR) to identify prolonged eye closure.
- Immediate audio alerts when drowsiness is detected.
- Lightweight and efficient implementation suitable for prototyping and demonstration.
- Basic image enhancement using OpenCV to improve detection in low-light conditions.

## Code Explanation & Key Algorithms
### Eye Aspect Ratio (EAR) Calculation
The core of the drowsiness detection system is the **Eye Aspect Ratio (EAR)**, a mathematical formula that quantifies eye openness using six specific facial landmarks around the eye.

#### EAR Formula

$$
EAR = \frac{||P_2 - P_6|| + ||P_3 - P_5||}{2 \times ||P_1 - P_4||}
$$

- P1 to P6 are the coordinates of key eye landmarks detected by Mediapipe.
- The numerator computes the sum of the vertical distances between the eyelids.
- The denominator computes the horizontal eye width.
- When the eye closes, the vertical distances shrink, causing the EAR to drop below a threshold.

#### Visual Representation

![image](https://github.com/user-attachments/assets/14dbcf0e-8a43-4360-94b3-59e21f80495b)


Below is a diagram showing the six eye landmarks and the distances used in the EAR calculation:
### How the Detection Logic Works
1. **Image Enhancement:**  
   Each frame is pre-processed using OpenCV to improve contrast and brightness, making facial features more visible in low-light conditions.

2. **Facial Landmark Detection:**  
   Mediapipe’s Face Mesh identifies 468 facial landmarks, from which specific points around both eyes are extracted.

3. **EAR Computation:**  
   The EAR is calculated for both eyes and averaged. If the EAR remains below a set threshold for a certain duration, the system infers drowsiness.

4. **Alert Mechanism:**  
   If drowsiness is detected, an alarm flag is set to trigger an audio or visual alert.

### Code Snippet: EAR Calculation
```python
def get_ear(landmarks, refer_idxs, frame_width, frame_height):
    coords_points = []
    for i in refer_idxs:
        lm = landmarks[i]
        coord = denormalize_coordinates(lm.x, lm.y, frame_width, frame_height)
        coords_points.append(coord)
    P2_P6 = distance(coords_points[1], coords_points[5])
    P3_P5 = distance(coords_points[2], coords_points[4])
    P1_P4 = distance(coords_points[0], coords_points[3])
    ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
    return ear, coords_points
```

### Example: State Tracking Logic
- The system uses timers to track how long the driver’s eyes remain closed.
- If the eyes are closed for longer than a preset "wait time," an alert is triggered.
- All relevant values (EAR, drowsy time) are displayed on the video feed for transparency.

## Reports
- A summary report with project motivation, methodology, and results is included for reference.
- Screenshots and sample outputs are provided to illustrate system performance.

## Future Work
- Integration with embedded hardware platforms (e.g., Raspberry Pi, Jetson Nano) for in-vehicle deployment.
- Enhancement of detection accuracy under varied lighting conditions (e.g., using infrared cameras or advanced preprocessing).
- Extension to monitor additional cues such as yawning or head tilt.
- Development of a user-friendly interface and mobile app for real-time monitoring.

## Creativity & Further Ideas
- **Personalization:** The system could adapt the EAR threshold for individual users, improving accuracy.
- **Data Logging:** Optionally log drowsiness events for later analysis, helping drivers understand their fatigue patterns.
- **Gamification:** Encourage safe driving by tracking alertness scores over time.

## Disclaimer
This project is a prototype developed for learning and demonstration purposes. The current implementation focuses on the core detection logic using computer vision; no hardware integration (such as pressure sensors or vibration pads) is included. The system is intended as a proof-of-concept and is not production-ready.

## Acknowledgements
The motivation, introduction, and general concepts for this project are inspired by prior research and academic reports on driver drowsiness detection. The implementation in this repository is based on open-source tools and libraries, with a focus on rapid prototyping and demonstration.

For any questions or suggestions, please contact the repository maintainer.
