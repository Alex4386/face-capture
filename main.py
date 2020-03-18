import cv2
from WebcamConnect import VideoStream
import WebcamConnect.Resolution as Resolution
import Persistent

vs = VideoStream(Persistent.Credentials.labCameraAddress)

vs.connect()

while True:
    frame = vs.getFrame(
        resolution=Resolution.FullHD
    )
    print("got frame!")
    cv2.imshow("Apple", frame)
    cv2.waitKey(5)
