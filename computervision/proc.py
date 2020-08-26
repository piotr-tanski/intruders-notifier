from typing import Tuple
import cv2

Resolution = Tuple[int, int]


class ImageProcessor:
    @classmethod
    def transform(cls, frame, resolution: Resolution):
        resized = cv2.resize(frame, resolution)
        return cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
