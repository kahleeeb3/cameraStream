from flask import Flask, Response
import cv2
import numpy as np
from picamera2 import Picamera2
from time import sleep

app = Flask(__name__)

# Initialize Picamera2
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()

# Frame capture function
def generate_video():
    while True:
        # Capture the frame from the camera
        np_array = picam2.capture_array()

        # Convert the frame to JPEG
        _, jpeg = cv2.imencode('.jpg', np_array)
        
        # Yield the frame in the MJPEG stream format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
