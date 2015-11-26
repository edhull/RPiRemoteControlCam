killall -s SIGINT mjpg_streamer
/usr/local/bin/mjpg_streamer -o "/usr/local/lib/output_http.so -w /home/ed/steamer-pi/mjpg-streamer/mjpg-streamer-experimental/www/ -p 1624" -i "/usr/local/lib/input_raspicam.so -x 640 -y 480 -fps 3 -ex night -sh 95 -br 55 -awb auto -ev 3 -co 5 -mm matrix "
