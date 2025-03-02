from flask import Flask, Response, render_template
import queue
import threading
from time import sleep
from picamera2 import Picamera2 # type: ignore
import cv2

# video parameters
resX = 640
resY = 360
fps = 15
imgQuality = 50
queue_size = 50

# define and start the camera
picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (resX, resY)})
picam2.configure(config)
picam2.start()

# create the queue
frame_queue = queue.Queue(maxsize=queue_size)

def capture_frames():
    while True:
        np_array = picam2.capture_array()
        rgb_array = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
        _, jpeg = cv2.imencode('.jpg', rgb_array, [int(cv2.IMWRITE_JPEG_QUALITY), imgQuality])
        frame_queue.put(jpeg.tobytes()) # if queue full, stop writing

def generate_video():
    while True:
        frame_data = frame_queue.get() # get frame data, if queue empty stop
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n\r\n')
        sleep(1/fps) # set frame rate by pausing

# thread to capture frames
capture_thread = threading.Thread(target=capture_frames)
capture_thread.daemon = True  # Thread exits when program exits
capture_thread.start()    

# configure flask
app = Flask(__name__)
@app.route('/video_feed')
def video_feed():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Stopping application")