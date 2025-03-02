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

<table class="wikitable sortable jquery-tablesorter">
<thead><tr>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Width
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Height
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name
</th></tr></thead><tbody>
<tr>
<td>640
</td>
<td>360
</td>
<td><a href="/wiki/Display_resolution_standards#640_×_360_(nHD)" title="Display resolution standards">nHD</a>
</td></tr>
<tr>
<td>854
</td>
<td>480
</td>
<td><a href="/wiki/Display_resolution_standards#FWVGA" title="Display resolution standards">FWVGA</a>
</td></tr>
<tr>
<td>960
</td>
<td>540
</td>
<td><a href="/wiki/Display_resolution_standards#qHD" title="Display resolution standards">qHD</a>
</td></tr>
<tr>
<td>1024
</td>
<td>576
</td>
<td><a href="/wiki/Display_resolution_standards#1024_×_576,_1024_×_600_(WSVGA)" title="Display resolution standards">WSVGA</a>
</td></tr>
<tr>
<td>1280
</td>
<td>720
</td>
<td><a href="/wiki/Display_resolution_standards#1280_×_720_(HD)" title="Display resolution standards">HD</a>
</td></tr>
<tr>
<td>1366
</td>
<td>768
</td>
<td><a href="/wiki/Display_resolution_standards#WXGA" title="Display resolution standards">FWXGA</a>
</td></tr>
<tr>
<td>1600
</td>
<td>900
</td>
<td><a href="/wiki/Display_resolution_standards#HD+" title="Display resolution standards">HD+</a>
</td></tr>
<tr>
<td>1920
</td>
<td>1080
</td>
<td><a href="/wiki/Display_resolution_standards#1920_×_1080_(FHD)" title="Display resolution standards">Full HD</a>
</td></tr>
<tr>
<td>2560
</td>
<td>1440
</td>
<td><a href="/wiki/Display_resolution_standards#2560_×_1440_(QHD)" title="Display resolution standards">QHD</a>
</td></tr>
<tr>
<td>3200
</td>
<td>1800
</td>
<td><a href="/wiki/Display_resolution_standards#QHD+" title="Display resolution standards">QHD+</a>
</td></tr>
<tr>
<td>3840
</td>
<td>2160
</td>
<td><a href="/wiki/Display_resolution_standards#4K_UHD" title="Display resolution standards">4K UHD</a>
</td></tr>
<tr>
<td>5120
</td>
<td>2880
</td>
<td><a href="/wiki/Display_resolution_standards#5120_×_2880_(5K_UHD)" title="Display resolution standards">5K</a>
</td></tr>
<tr>
<td>7680
</td>
<td>4320
</td>
<td><a href="/wiki/Display_resolution_standards#8K_UHD" title="Display resolution standards">8K UHD</a>
</td></tr></tbody><tfoot></tfoot></table>