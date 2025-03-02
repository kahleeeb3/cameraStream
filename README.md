# Setup / Testing
## picamera2
<!-- https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf -->
### Testing
```
rpicam-hello
```
### Updating
```shell
sudo apt install -y python3-picamera2 --no-install-recommends # install with no GUI dependencies
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