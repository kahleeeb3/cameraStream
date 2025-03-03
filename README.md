# Setup / Testing
https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
## picamera2
<!-- https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf -->
### Testing
```
rpicam-hello
```
### Updating
```shell
sudo apt install -y python3-picamera2 --no-install-recommends # install with no GUI dependencies
# remove --no-install-recommends for GUI
```
### Testing python
```python
from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (680, 480)})
picam2.configure(config)

picam2.start()

picam2.capture_file("demo.jpg")
picam2.stop()
```
### Virtual Env
If the test script is only working outside the venv, start a new terminal and run:
```bash
python3 -m venv --system-site-packages env
source env/bin/activate
python main.py
```

# open-cv
```bash
sudo apt install -y python3-opencv
sudo apt install -y opencv-data
```

# H264 Video Recording
```python
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

picam2 = Picamera2()
video_config = picam2.create_video_configuration(
    main={"size": (800, 480), "format": "YUV420"}, #Using YUV420 is much more efficient for video.
    controls={"FrameRate": 30} #Set your desired framerate.
)
picam2.configure(video_config)

encoder = H264Encoder(5000000)  # Adjust bitrate as needed (5 Mbps in this example)

picam2.start_recording(encoder, 'test.h264')
print("Recording started...")
time.sleep(3)  # Record for 10 seconds (adjust as needed)
picam2.stop_recording()
print("Recording stopped.")

picam2.close() #Close the camera.
```