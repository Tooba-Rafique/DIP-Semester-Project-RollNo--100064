<h1 align="center">🚦 DIP Semester Project</h1>
<h2 align="center">Traffic Violation Detection System</h2>

<p align="center">
<b>Course:</b> Digital Image Processing <br>
<b>Student:</b> Tooba Rafique &nbsp; | &nbsp; <b>Roll No:</b> 100064
</p>

<hr>

<h2>📌 Project Overview</h2>

<p style="font-size:18px;">
This project presents an automated <b>Traffic Violation Detection System</b> developed using
<b>Digital Image Processing (DIP)</b> techniques. The system monitors traffic signals and vehicle
movement to detect red-light violations in real time. By analyzing signal color and vehicle position
relative to a predefined stop line, the system identifies and flags violating vehicles automatically.
</p>

<hr>

<h2>🎯 Project Objectives</h2>

<p style="font-size:18px;">
• Detect traffic signal status (Red / Green) using HSV color segmentation <br>
• Detect moving vehicles using Background Subtraction (MOG2) <br>
• Track vehicle movement near the stop line <br>
• Identify and flag violations when vehicles cross the stop line during a red signal <br>
• Reduce noise using Morphological Operations for cleaner detection
</p>

<hr>

<h2>🛠 Tools & Technologies</h2>

<p style="font-size:18px;">
• <b>Python</b> – Core programming language <br>
• <b>OpenCV</b> – Image and video processing <br>
• <b>NumPy</b> – Numerical operations and array handling
</p>

<hr>

<h2>⚙️ System Workflow</h2>

<p style="font-size:18px;">
1. Input traffic video is loaded into the system <br>
2. Traffic signal color is detected using HSV color space <br>
3. Vehicles are detected using background subtraction <br>
4. Vehicle position is analyzed relative to the stop line <br>
5. If the signal is red and a vehicle crosses the stop line, a violation is flagged
</p>

<hr>

<h2>▶ How to Run the Project</h2>

<p style="font-size:18px;">
1. Clone this repository to your local machine <br>
2. Place the traffic video file in the project directory and name it:
<b>traffic_video.mp4</b> <br>
3. Install required libraries using:
</p>

<pre>
pip install opencv-python numpy
</pre>

<p style="font-size:18px;">
4. Navigate to the project folder and run:
</p>

<pre>
python main.py
</pre>

<hr>

<h2>📊 Output</h2>

<p style="font-size:18px;">
The system displays bounding boxes around detected vehicles and labels any vehicle that violates
traffic rules during a red signal. This output helps visualize real-time violation detection clearly.
</p>

<hr>

<h2>✅ Conclusion</h2>

<p style="font-size:18px;">
This project demonstrates the practical application of Digital Image Processing in traffic
management systems. By combining color detection and motion tracking, the system provides an
effective and automated solution for identifying traffic signal violations, contributing to improved
road safety and efficient monitoring.
</p>

<hr>

<p align="center">
<b>Digital Image Processing – Semester Project</b>
</p>
