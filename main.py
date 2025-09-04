from typing import T
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start() # i don't know if this is necessary

while True:
    pass
