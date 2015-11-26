# Raspberry Pi Remote Control X/Y Camera
### Installation
(These instructions are most likely incomplete! Personalise/modify them to your setup)
```sh
$ sudo apt-get install python-dev python-rpi.gpio python-pip motion
```
```sh
$ sudo pip install flask
```
```sh
$ git clone https://github.com/jacksonliam/mjpg-streamer
```
```sh
$ ./mjpg-streamer.sh &
```
```sh
$ python picam.py &
```


mjpg-stream.sh will run the Flask web server and will receive button presses, whilst picam.py will control streaming the camera data. Both scripts must be running simultaneously. A cleaner solution is to run each script inside a Screen window on boot via /etc/rc.local:

```sh
echo "Starting python webserver..."
screen -S python -dm bash -c 'python /home/user/picam.py;exec bash'
echo "Starting webcam stream..."
screen -S webcamstream -dm bash -c '/home/user/mjpg-stream.sh;exec bash'
exit 0
```

If you want to record footage from the camera, you can use Motion.
```sh
$ sudo apt-get install motion
```
... and modify the /etc/motion/motion.conf file to use the camera stream as an input rather than a USB webcam (as well as a bunch of other settings!)
```sh
# URL to use if you are using a network camera, size will be autodetected (incl http:// ftp:// or file:///)
# Must be a URL that returns single jpeg pictures or a raw mjpeg stream. Default: Not defined
netcam_url http://127.0.0.1:1111/?action=stream 
```

### Hardware
  - No-IR Camera
  - X/Y Camera Servo Platform (http://www.amazon.co.uk/Camera-Platform-Mount-MG90S-Servos/dp/B00BUBDSMA)

### Dependencies
  - MJPG-Steamer Fork (https://github.com/jacksonliam/mjpg-streamer)
  - Python 2.7+
  - Flask (A micro python-based web server)
  - RPi.GPIO Library (https://pypi.python.org/pypi/RPi.GPIO)

### Further reading:

  - https://www.raspberrypi.org/forums/viewtopic.php?t=45178
  
### Version
v1.0
Ed Hull (11/2015)


