#
# Script that finds faces
#
# import standard library modules
import sys
from time import sleep
# import 3rd party modules
import cv2
import RPi.GPIO as GPIO
# ----------------------------------------------------------------------------
def dc_motor_init():
    'init the pins and motors'
    GPIO.setmode(GPIO.BOARD)
    # dict with the motor and the pin number
    motor_dict = {'motor_1a': 7,
                  'motor_1b': 11,
                  'motor_1e': 15,
                  'motor_2a': 10,
                  'motor_2b': 8,
                  'motor_2e': 12,
                  'motor_3a': 19,
                  'motor_3b': 21,
                  'motor_3e': 23,
                 }
    # init the gpio pins
    for gpio in motor_dict:
        GPIO.setup(motor_dict[gpio], GPIO.OUT)
        sleep(0.1)
        print('set up pin ' + gpio)
    return(motor_dict)
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    motor_dict = dc_motor_init()
    print('motor init done')
    sleep(1)
    casc_path = '/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml'

    # create the haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    cap = cv2.VideoCapture(0)
    
    try:
        while True:
            # Capture frame by frame
            ret, frame = cap.read()
            if ret:
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
                    print('found face')
                    
                    GPIO.output(motor_dict['motor_1a'], GPIO.HIGH)      
                    GPIO.output(motor_dict['motor_1b'], GPIO.LOW)
                    GPIO.output(motor_dict['motor_1e'], GPIO.HIGH)
                sleep(1)
                GPIO.output(motor_dict['motor_1e'], GPIO.LOW)

    except KeyboardInterrupt:
        print('Keyboard interrupt: Cleaned up programme')
        GPIO.cleanup()
        cap.release()
    except Exception:
        GPIO.cleanup()
        cap.release()
