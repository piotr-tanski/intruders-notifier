import computervision as cv
import emailnotifier as email


if __name__ == '__main__':
    # connect to the default camera by default.
    camera = cv.Camera()
    detector = cv.PeopleDetector()
    notifier = email.Notifier()
    try:
        while True:
            success, frame = camera.grab()
            if not success:
                continue

            transformed = cv.ImageProcessor.transform(frame, (640, 480))
            if detector.detected(transformed):
                print('A person detected')
                notifier.send()
    except KeyboardInterrupt:
        print('Program interrupted. Closing...')
    finally:
        camera.destroy()
