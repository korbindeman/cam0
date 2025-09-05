from ..request import MappedArray as MappedArray
from _typeshed import Incomplete
from picamera2.encoders.encoder import Encoder as Encoder, Quality as Quality

class LibavH264Encoder(Encoder):
    repeat: Incomplete
    bitrate: Incomplete
    iperiod: Incomplete
    framerate: Incomplete
    qp: Incomplete
    profile: Incomplete
    preset: Incomplete
    drop_final_frames: bool
    threads: int
    def __init__(self, bitrate=None, repeat: bool = True, iperiod: int = 30, framerate: int = 30, qp=None, profile=None) -> None: ...
    @property
    def use_hw(self): ...
    @use_hw.setter
    def use_hw(self, value) -> None: ...
