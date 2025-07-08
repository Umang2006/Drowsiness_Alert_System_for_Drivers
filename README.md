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

## Future Work

- Integration with embedded hardware platforms (e.g., Raspberry Pi, Jetson Nano) for in-vehicle deployment.
- Extension to monitor additional cues such as yawning or head tilt.
- Development of a user-friendly interface and mobile app for real-time monitoring.
