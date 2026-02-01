import cv2
import numpy as np

# -------------------------------
# Video Input
# -------------------------------
cap = cv2.VideoCapture("traffic_video.mp4")

if not cap.isOpened():
    print("Error: traffic_video.mp4 not found!")
    exit()

# Background Subtractor
bg = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=False
)

STOP_LINE_Y = 300

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (800, 500))

    # -------------------------------
    # PROJECT TITLE (Only This Text)
    # -------------------------------
    cv2.putText(frame,
                "Monitoring System",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 255, 255), 2)

    # -------------------------------
    # SIGNAL DETECTION (INTERNAL USE)
    # -------------------------------
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red signal
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    red_signal = cv2.countNonZero(red_mask) > 500

    # Green signal
    lower_green = np.array([36, 50, 70])
    upper_green = np.array([89, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green_signal = cv2.countNonZero(green_mask) > 500

    # -------------------------------
    # VEHICLE DETECTION
    # -------------------------------
    fgmask = bg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    clean = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        clean,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw stop line
    cv2.line(frame,
             (0, STOP_LINE_Y),
             (frame.shape[1], STOP_LINE_Y),
             (255, 0, 0), 2)

    # -------------------------------
    # LOGIC ACCORDING TO SIGNAL RULE
    # -------------------------------
    for cnt in contours:
        if cv2.contourArea(cnt) > 2000:
            x, y, w, h = cv2.boundingRect(cnt)

            # GREEN SIGNAL → Vehicle allowed to move
            if green_signal:
                cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (0, 255, 0), 2)

            # RED SIGNAL → Vehicle should stop
            elif red_signal:
                cv2.rectangle(frame,
                              (x, y),
                              (x + w, y + h),
                              (0, 0, 255), 2)

                # Violation only if vehicle crosses stop line
                if y + h > STOP_LINE_Y:
                    cv2.putText(frame,
                                "Red Signal Violation",
                                (x, y - 8),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (0, 0, 255), 2)

    cv2.imshow("Traffic Monitoring", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
