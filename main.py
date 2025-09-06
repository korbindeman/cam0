import os
from datetime import datetime

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget

from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2

picam2 = Picamera2()

picam2.configure(picam2.create_preview_configuration())

CAPTURE_DIR = os.path.expanduser("~/Pictures/captures")
os.makedirs(CAPTURE_DIR, exist_ok=True)


def capture(format):
    if format not in ["png", "jpg"]:
        return

    cfg = picam2.create_still_configuration()

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(CAPTURE_DIR, f"{ts}.{format}")

    picam2.switch_mode_and_capture_file(
        cfg, filename, signal_function=qpicamera2.signal_done
    )


def on_button_clicked():
    shutter_button.setEnabled(False)
    capture("png")


def capture_done(job):
    result = picam2.wait(job)
    shutter_button.setEnabled(True)


app = QApplication([])

qpicamera2 = QGlPicamera2(picam2, width=800, height=600, keep_ar=True)

shutter_button = QPushButton("Capture")
quit_button = QPushButton("Quit")

window = QWidget()

qpicamera2.done_signal.connect(capture_done)
shutter_button.clicked.connect(on_button_clicked)
quit_button.clicked.connect(quit)

layout_v = QVBoxLayout()
layout_v.addWidget(qpicamera2)

layout_v.addWidget(shutter_button)
layout_v.addWidget(quit_button)

window.setWindowTitle("cam0")
window.setLayout(layout_v)

picam2.start()

window.showFullScreen()

# window.resize(640, 480)
# window.show()

app.exec()
