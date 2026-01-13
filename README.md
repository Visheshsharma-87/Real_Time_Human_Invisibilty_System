# Real-Time Human Invisibility System using MediaPipe
This project implements a real-time human invisibility system using
machine learning–based human segmentation. The system removes the entire
human body from live webcam footage and replaces it with the previously
captured background, creating an invisibility illusion.

Unlike traditional approaches that depend on detecting a specific
clothing color, this project works independently of clothing color and
lighting variations.

# Introduction
Invisibility effects are commonly implemented using color-based
segmentation, where a specific color (such as red or green) is removed
from the video frame. These methods are unreliable in real-world
conditions because they fail when the clothing color changes or when
lighting conditions vary.

This project overcomes those limitations by using a machine
learning–based human segmentation model. The system detects the human
body at a pixel level and removes it entirely from the scene.

# Objective
The main objective of this project is to:
- Detect the human body in real time using a lightweight ML model
- Remove the detected human region from the video frame
- Replace it with the background captured earlier
- Achieve smooth real-time performance on CPU-based systems

# Methodology
The project follows the steps below:
1. Capture live video frames using a webcam
2. Automatically capture the background when no human is present
3. Apply MediaPipe Selfie Segmentation to obtain a human segmentation mask
4. Identify pixels belonging to the human body
5. Replace those pixels with the corresponding background pixels
6. Display the final output frame in real time

This approach allows complete invisibility of the human body regardless
of clothing color or pose.

# Technologies Used
- Python
- OpenCV for video capture and image processing
- MediaPipe for real-time human segmentation
- NumPy for numerical and array operations

# System Requirements
- Python version 3.8 to 3.11
- Functional webcam
- CPU-based system (GPU not required)
The project has been tested on an Intel i3 11th Generation laptop and
runs smoothly in real time.

# Project Structure
InvisibleHuman_MediaPipe/
│
├── main.py # Main execution file
├── utils.py # Utility functions (FPS counter and text overlay)
├── requirements.txt # List of dependencies
│
├── assets/
│ └── demo.png # Output screenshot (to be added)
│
└── output/
## Installation and Execution
Step 1: Install the required dependencies
pip install -r requirements.txt

Step 2: Run the project python main.py

Step 3: Usage instructions
- Stay out of the camera frame for the first few seconds
- The background will be captured automatically
- Step into the frame to observe the invisibility effect
- Press the `q` key to exit the application safely

## Performance
- Real-time execution on CPU-based systems
- Average frame rate of 15 to 25 FPS on an Intel i3 processor
- Stable execution without system freezing
- Works with any clothing color

## Applications
- Computer vision demonstrations
- Augmented reality experiments
- Academic mini and major projects
- Machine learning portfolio projects

## Limitations
- The quality of invisibility depends on accurate background capture
- Sudden background changes may reduce visual accuracy
- Performance may vary on very low-end hardware

## Developer
Vishesh Sharma for contact use Email:- sharmavishesh308@gmail.com

## Conclusion
This project demonstrates a practical application of machine learning
in real-time computer vision. By using MediaPipe instead of heavy deep
learning models, the system achieves a balance between accuracy and
performance, making it suitable for deployment on standard laptops
without GPU support.





