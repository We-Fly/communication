# 这个文件是描述飞机类的
from .Serial import *
from .NClink import *
from .ACLink import *

class UAV:
    _height = 0
    _isUnlock = False
    _protocol = None

    def __init__(self, protocol) -> None:
        self._height = 0
        self._isUnlock = False
        self._protocol = protocol()
        
    def unlock(self,):
        self._isUnlock = True

    def lock(self,):
        self._isUnlock = False

    def takeoff(self):
        self.unlock()

    def setHeight(self, height):
        pass

    def setYaw(self, yaw):
        pass
    
    def setX(self, x):
        pass
    
    def setY(self, y):
        pass

    def landing():
        pass
