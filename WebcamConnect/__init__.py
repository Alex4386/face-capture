import cv2
import WebcamConnect.Resolution as Resolution


class VideoStream():
    connected = False

    def __init__(self, videoStream):
        self.videoStream = videoStream

    def connect(self):
        self.vc = cv2.VideoCapture(self.videoStream)

        while not self.vc.isOpened():
            pass

        self.connected = True
        return

    def disconnect(self):
        self.vc.release()
        self.connected = False

    def isConnected(self):
        return self.connected

    def getFrame(self, resolution=None):
        success, tmpFrame = self.vc.read()
        if resolution is not None:
            tmpFrame = cv2.resize(tmpFrame, resolution)

        return tmpFrame
