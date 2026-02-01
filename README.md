# DIP-Semester-Project-RollNo--100064
TrafficViolation-Dectection

​Student Information:

​Name: Tooba Rafique
​Roll Number: 100064
​Course: Digital Image Processing

​Project Description:
​This project is an automated traffic monitoring system designed to detect vehicles that violate red light signals. It uses Digital Image Processing to identify the traffic light color and track vehicle movement relative to a defined stop line.​The system automatically flags any vehicle crossing the line during a red signal, helping in efficient law enforcement. It reduces the need for manual surveillance and enhances road safety through real-time detection.

​Project Objectives:
​Signal Status Detection: Using color-based HSV segmentation to identify Red/Green lights.
​Vehicle Detection: Utilizing Background Subtractor (MOG2) and Contour detection to find moving cars.
​Violation Logic: flagging vehicles that cross the Stop Line when the signal is Red.
​Noise Reduction: Applying Morphological Operations (Closing) for a cleaner image.

​Tools & Technologies Used:
​Python: Main programming language.
​OpenCV: For image and video processing.
​NumPy: For handling image arrays.

​Steps to Run the Code:
​Clone Repository: Copy the project to your local machine.
​Video File: Place your video named traffic_video.mp4 in the project folder.
​Install Libraries: Run pip install opencv-python numpy in your terminal.
​Run Script: Navigate to the Code/ folder and type python main.py.

​Conclusion:
​The system successfully integrates color detection and motion tracking to identify signal violators. This demonstrates how DIP provides a reliable, automated solution for modern traffic management.
