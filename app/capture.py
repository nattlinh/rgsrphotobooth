import cv2 as cv

cam = cv.VideoCapture(0)

def gen_frame():
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        ret, buffer = cv.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        #cv.imshow("Photo", cv.flip(image, 1))

    cam.release()

cam.release()
cv.destroyAllWindows()
'''
        yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + cv.imencode('.jpg', image)[1].tobytes() + b'\r\n')

        if cv.waitKey(1) & 0xff == ord(' '):
            cv.imwrite("Photo.png", cv.flip(image, 1))
            break
        '''