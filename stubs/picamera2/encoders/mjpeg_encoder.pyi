from picamera2.encoders import Quality as Quality
from picamera2.encoders.v4l2_encoder import V4L2Encoder as V4L2Encoder

class MJPEGEncoder(V4L2Encoder):
    def __init__(self, bitrate=None) -> None: ...
