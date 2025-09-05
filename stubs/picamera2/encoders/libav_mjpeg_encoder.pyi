from ..request import MappedArray as MappedArray
from _typeshed import Incomplete
from picamera2.encoders.encoder import Encoder as Encoder, Quality as Quality

class LibavMjpegEncoder(Encoder):
    repeat: Incomplete
    bitrate: Incomplete
    iperiod: Incomplete
    framerate: Incomplete
    qp: Incomplete
    def __init__(self, bitrate=None, repeat: bool = True, iperiod: int = 30, framerate: int = 30, qp=None) -> None: ...
