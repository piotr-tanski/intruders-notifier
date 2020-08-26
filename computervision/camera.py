import cv2


class Camera:
    def __init__(self, device_index: int = 0):
        self.__cap = cv2.VideoCapture(device_index)

    def grab(self):
        return self.__cap.read()

    def destroy(self):
        self.__cap.release()
