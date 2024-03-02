import cv2 as cv

cam = cv.VideoCapture(0)

def gen_frame():
    while True:
        ret, frame = cam.read()
        frame = cv.flip(frame, 1)
        if not ret:
            break
        
        # Extract the encoded image data from the tuple
        _, buffer = cv.imencode('.jpg', frame)  # Use unpacking to avoid naming the first element
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        
        if cv.waitKey(1) & 0xff == ord(' '):
            cv.imwrite("Photo.png", frame)
            break

    cam.release()