from _typeshed import Incomplete
from picamera2.encoders import Quality as Quality
from picamera2.encoders.v4l2_encoder import V4L2Encoder as V4L2Encoder

class H264Encoder(V4L2Encoder):
    iperiod: Incomplete
    repeat: Incomplete
    qp: Incomplete
    profile: Incomplete
    framerate: Incomplete
    def __init__(self, bitrate=None, repeat: bool = True, iperiod=None, framerate=None, enable_sps_framerate: bool = False, qp=None, profile=None) -> None: ...
