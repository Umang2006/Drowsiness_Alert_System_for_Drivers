# DrowSee: Driver Drowsiness Detection System

## Overview

**DrowSee** is a real-time driver drowsiness detection system designed to enhance road safety by identifying early signs of driver fatigue. The project leverages advanced computer vision techniques to monitor behavioral cues, such as eye movements, and provides timely alerts to prevent potential accidents. This repository contains the code and resources for the implementation using Python, OpenCV, and Mediapipe.

## Motivation

Driver fatigue is a significant contributor to road accidents worldwide, often resulting in impaired reaction times and poor decision-making. Many drivers underestimate the impact of drowsiness, making proactive detection systems crucial for safety. DrowSee aims to address this challenge by offering a distraction-free, real-time monitoring solution that can be integrated seamlessly into the driving experience.

## Project Objectives

- **Accurately detect signs of driver drowsiness** using facial landmark analysis and eye aspect ratio (EAR) computation.
- **Provide real-time alerts** to drivers when drowsiness is detected, enabling timely corrective action.
- **Design a modular and adaptable system** that can be further extended for embedded or in-vehicle deployment.
- **Promote road safety** by reducing the risk of accidents caused by driver fatigue.

## Features

- Real-time video processing from a standard webcam.
- Facial landmark detection using Mediapipe for robust eye tracking.
- Calculation of Eye Aspect Ratio (EAR) to identify prolonged eye closure.
- Immediate audio alerts when drowsiness is detected.
- Lightweight and efficient implementation suitable for prototyping and demonstration.

## Usage

1. **Clone this repository** and install the required dependencies listed in `requirements.txt`.
2. **Run the main script** to start real-time drowsiness detection using your computer’s webcam.
3. **Follow on-screen instructions**; an audible alert will sound if drowsiness is detected.

## Reports

- A summary report with project motivation, methodology, and results is included for reference.
- Screenshots and sample outputs are provided to illustrate system performance.

## Disclaimer

This project is a prototype developed for learning and demonstration purposes. The current implementation focuses on the core detection logic using computer vision; no hardware integration (such as pressure sensors or vibration pads) is included. The system is intended as a proof-of-concept and is not production-ready.

## Future Work

- Integration with embedded hardware platforms (e.g., Raspberry Pi, Jetson Nano) for in-vehicle deployment.
- Enhancement of detection accuracy under varied lighting conditions.
- Extension to monitor additional cues such as yawning or head tilt.
- Development of a user-friendly interface and mobile app for real-time monitoring.

## Acknowledgements

The motivation, introduction, and general concepts for this project are inspired by prior research and academic reports on driver drowsiness detection. The implementation in this repository is based on open-source tools and libraries, with a focus on rapid prototyping and demonstration.

For any questions or suggestions, please contact the repository maintainer.

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51914927/8b459308-b379-4607-9462-829d387677d8/Design-project-Drowsiness-1.pdf
