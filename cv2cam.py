import cv2

class CV2Camera:
    def __init__(self) -> None:
        pass
    
    def get_frame(self):
        self.cam = cv2.VideoCapture(0)
        ret, frame = self.cam.read()
        if not ret:
            return
        cv2.imwrite("frame.png", frame)
        self.cam.release()