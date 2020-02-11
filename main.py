from WebcamConnect import VideoStream
import WebcamConnect.Resolution as Resolution
import Persistent
import cv2

vs = VideoStream(Persistent.Credentials.labCameraAddress)

vs.connect()

while True:
    frame = vs.getFrame(
        resolution=Resolution.FullHD
    )
    cv2.imshow("Apple", frame)
    cv2.waitKey(5)
