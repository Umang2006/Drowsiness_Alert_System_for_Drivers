# DrowSee: Driver Drowsiness Detection System

## Overview

**DrowSee** is a real-time driver drowsiness detection system designed to enhance road safety by identifying early signs of driver fatigue. The project leverages advanced computer vision techniques to monitor behavioral cues, such as eye movements, and provides timely alerts to prevent potential accidents. This repository contains the code and resources for the implementation using Python, OpenCV, and Mediapipe.

## Motivation

Driver fatigue is a significant contributor to road accidents worldwide, often resulting in impaired reaction times and poor decision-making. Many drivers underestimate the impact of drowsiness, making proactive detection systems crucial for safety. DrowSee aims to address this challenge by offering a distraction-free, real-time monitoring solution that can be integrated seamlessly into the driving experience.

## Key Features

- **Real-Time Monitoring:** Processes live video to detect and analyze facial landmarks.
- **Eye Aspect Ratio (EAR) Analysis:** Calculates EAR to identify prolonged eye closure, a key indicator of drowsiness.
- **Image Enhancement:** Utilizes OpenCV techniques such as histogram equalization and brightness/contrast adjustment to improve detection accuracy in low-light conditions.
- **Immediate Alerts:** Displays visual warnings when drowsiness is detected.
- **Modular Design:** Easily extensible for additional features or hardware integration.

## How It Works

1. **Video Capture:** The system captures frames from a standard webcam.
2. **Image Enhancement:** Each frame is enhanced using OpenCV to improve visibility, especially in low-light environments.
3. **Facial Landmark Detection:** Mediapipe Face Mesh identifies key eye landmarks in each frame.
4. **EAR Calculation:** The Eye Aspect Ratio is computed for both eyes and averaged.
5. **Drowsiness Detection:** If the EAR remains below a set threshold for a specified duration, the system flags potential drowsiness and displays an alert.


## Future Work

- Integration with embedded hardware platforms (e.g., Raspberry Pi, Jetson Nano) for in-vehicle deployment.
- Advanced detection under challenging conditions (e.g., extreme lighting, occlusions).
- Expansion to monitor additional cues such as yawning or head movement.
- Development of a user-friendly interface and audio alert system.
