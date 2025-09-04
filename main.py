import os
from datetime import datetime
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from picamera2 import Picamera2
from picamera2.previews.qt import QGlPicamera2

# Ensure capture folder exists
CAPTURE_DIR = os.path.expanduser("~/Pictures/captures")
os.makedirs(CAPTURE_DIR, exist_ok=True)

picam2 = Picamera2()

class View(QGlPicamera2):
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position()
            print(f"Tap at: {pos.x():.0f}, {pos.y():.0f}")

            # Generate timestamped filename
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(CAPTURE_DIR, f"{ts}.jpg")

            picam2.capture_file(filename)
            print(f"Saved: {filename}")

        super().mousePressEvent(event)

app = QApplication([])
view = View(picam2, width=1280, height=720)
view.setWindowTitle("Tap to Capture")
view.showFullScreen()

picam2.start()
app.exec()
