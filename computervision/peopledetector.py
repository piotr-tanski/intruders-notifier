import cv2


class PeopleDetector:
    def __init__(self):
        self.__hog = cv2.HOGDescriptor()
        self.__hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detected(self, frame) -> bool:
        boxes, _ = self.__hog.detectMultiScale(frame, winStride=(8, 8))
        return len(boxes) > 0
