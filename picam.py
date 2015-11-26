import RPi.GPIO as GPIO
import time
import atexit
from time import sleep
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

panDegrees = 14.5
tiltDegrees = 16.5

dc = 100.0 # duty cycle (0-100) for PWM pin

pan = GPIO.PWM(12, dc)
pan.start(panDegrees)
sleep(0.4)
pan.stop()

tilt = GPIO.PWM(33, dc)
tilt.start(tiltDegrees)
sleep(0.4)
tilt.stop()


# Cleanup any open objects
def cleanup():
    GPIO.cleanup()

# Load the main form template on webrequest for the root page
@app.route("/cameracontrol")
def main():

    # Create a template data dictionary to send any data to the template
    templateData = {
        'title' : 'Camera'
        }
    # Pass the template data into the template picam.html and return it to the user
    return render_template('picam.html', **templateData)


# The function below is executed when someone requests a URL with a move direction
@app.route("/<path:path>")
def move(path):
    global panDegrees
    global tiltDegrees
    if path.endswith('right'):
            if panDegrees > 5:
                        panDegrees = panDegrees - 0.5
                        print("%s : %s" % (panDegrees, tiltDegrees))
                        pan = GPIO.PWM(12, dc) 
                        pan.start(panDegrees)
			sleep(0.25)
                        pan.stop()
            return str(panDegrees)
    elif path.endswith('left'):
            if panDegrees < 25:
                        panDegrees = panDegrees + 0.5
	                print("%s : %s" % (panDegrees, tiltDegrees)) 
			pan = GPIO.PWM(12, dc)
                        pan.start(panDegrees)
                        sleep(0.25)
                        pan.stop()
            return str(panDegrees)
    elif path.endswith('down'):
            if tiltDegrees < 24:
                        tiltDegrees = tiltDegrees + 0.5
                        print("%s : %s" % (panDegrees, tiltDegrees))
                        tilt = GPIO.PWM(33, dc)
                        tilt.start(tiltDegrees)
                        sleep(0.25)
                        tilt.stop()
            return str(tiltDegrees)
    elif path.endswith('up'):
            if tiltDegrees > 4:
                        tiltDegrees = tiltDegrees - 0.5
                        print("%s : %s" % (panDegrees, tiltDegrees))
                        tilt = GPIO.PWM(33, dc)
                        tilt.start(tiltDegrees)
                        sleep(0.25)
                        tilt.stop()
            return str(tiltDegrees)
    elif path.endswith('center'):
            tiltDegrees = 16.5
            print("%s : %s" % (panDegrees, tiltDegrees))
            tilt = GPIO.PWM(33, dc)
            tilt.start(tiltDegrees)

            panDegrees = 14.5
            print("%s : %s" % (panDegrees, tiltDegrees))
            pan = GPIO.PWM(12, dc)
            pan.start(panDegrees)

            sleep(1.2)
            tilt.stop()
            pan.stop()

            return "Centered all to 13"
    elif path.endswith('posOne'):
            tiltDegrees = 14.5
            print("%s : %s" % (panDegrees, tiltDegrees))
            tilt = GPIO.PWM(33, dc)
            tilt.start(tiltDegrees)

            panDegrees = 18.0
            print("%s : %s" % (panDegrees, tiltDegrees))
            pan = GPIO.PWM(12, dc)
            pan.start(panDegrees)

            sleep(0.5)
            tilt.stop()
            pan.stop()

            return "posOne"
    elif path.endswith('posTwo'):
            tiltDegrees = 13.0
            print("%s : %s" % (panDegrees, tiltDegrees))
            tilt = GPIO.PWM(33, dc)
            tilt.start(tiltDegrees)

            panDegrees = 15.0
            print("%s : %s" % (panDegrees, tiltDegrees))
            pan = GPIO.PWM(12, dc)
            pan.start(panDegrees)

            sleep(0.5)
            tilt.stop()
            pan.stop()

            return "posOne"
    elif path.endswith('posThree'):
            tiltDegrees = 10.5
            print("%s : %s" % (panDegrees, tiltDegrees))
            tilt = GPIO.PWM(33, dc)
            tilt.start(tiltDegrees)

            panDegrees = 15.0
            print("%s : %s" % (panDegrees, tiltDegrees))
            pan = GPIO.PWM(12, dc)
            pan.start(panDegrees)

            sleep(0.5)
            tilt.stop()
            pan.stop()

            return "posThree" 
    elif path.endswith('reset'):
            GPIO.cleanup()            
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(12, GPIO.OUT)
            GPIO.setup(33, GPIO.OUT)
            return "Reset!"

# Clean everything up when the app exits
atexit.register(cleanup)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
