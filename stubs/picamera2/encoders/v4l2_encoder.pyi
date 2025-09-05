from videodev2 import *
from _typeshed import Incomplete
from picamera2.encoders.encoder import Encoder as Encoder

class V4L2Encoder(Encoder):
    bufs: Incomplete
    bitrate: Incomplete
    vd: Incomplete
    framerate: Incomplete
    def __init__(self, bitrate, pixformat) -> None: ...
    def thread_poll(self, buf_available) -> None: ...
