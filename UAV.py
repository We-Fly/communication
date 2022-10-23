# 这个文件是描述飞机类的
from .Serial import *
from .NClink import *

class UAV:
    __height = 0
    __isUnlock = False
    __protocol = ""
    __serialPort = ""

    def __init__(self, port, protocol="NCLink", baudrate=115200) -> None:
        self.__height = 0
        __isUnlock = False
        __serialPort = port
        __protocol = protocol
        
    def unlock(self,):
        __isUnlock = True

    def lock(self,):
        __isUnlock = False

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