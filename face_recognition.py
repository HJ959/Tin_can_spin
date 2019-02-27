#
# Script that finds faces 
#

# import standard library modules
import sys

# import 3rd party modules
import cv2

if __name__ == '__main__':
    # Casc path and webcam setup
    cap = cv2.VideoCapture(0)
    casc_path = '/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml'
    #casc_path = '/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml'
    # create the haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    while True:
        # Capture frame by frame
        ret, frame = cap.read()
        
        # operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=7,
                                             minSize=(30, 30),
                                             flags=cv2.CASCADE_SCALE_IMAGE
                                             )

        for (x, y, w, h) in faces:
            print(x,y,w,h)
        #print('Found {0} faces!'.format(len(faces)))

    # when everythings done, release the capture
    cap.release()
    cv2.destroyAllWindows()

