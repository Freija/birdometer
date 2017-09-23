from gpiozero import MotionSensor, LED
from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()
camera.iso = 400

DATA_DIR = '/data/'

pir = MotionSensor(14)
try:
    while True:
        pir.wait_for_motion()
        filename = '{}{}'.format(DATA_DIR, datetime.now().strftime("%Y-%m-%d_%H.%M.%S"))
        print 'Bird alert ! -- ' + filename
        camera.start_preview()
        sleep(0.5)
        for i in range(10):
            camera.capture('%s_%i.jpg' % (filename, i))
        #pir.wait_for_no_motion()
        #print 'Motion stopped!'
        #camera.capture('%s_reference.jpg' % (filename))    
        #camera.stop_preview()
except KeyboardInterrupt:
    print 'Keyboard Interrupt caught!'


