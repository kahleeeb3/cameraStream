import cv2
from flask import Flask, Response, render_template
from picamera2 import Picamera2
import threading
import queue
import time

app = Flask(__name__)

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (320, 240)})  # Lower resolution
picam2.configure(config)
picam2.start()

frame_queue = queue.Queue(maxsize=10)  # Limit the queue size

def capture_frames():
    while True:
        try:
            np_array = picam2.capture_array()
            rgb_array = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
            _, jpeg = cv2.imencode('.jpg', rgb_array, [int(cv2.IMWRITE_JPEG_QUALITY), 80])  # Lower JPEG quality
            try:
                frame_queue.put(jpeg.tobytes(), timeout=1)  # Add timeout to prevent blocking
            except queue.Full:
                pass  # Drop frames if queue is full
        except Exception as e:
            print(f"Capture error: {e}")
            time.sleep(1) #avoid tight loop on error.

def generate_video():
    while True:
        try:
            frame_data = frame_queue.get(timeout=1)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n\r\n')
        except queue.Empty:
            continue  # Skip if queue is empty
        except Exception as e:
            print(f"Generate error: {e}")
            time.sleep(1)

# Start the frame capture thread before app.run()
capture_thread = threading.Thread(target=capture_frames)
capture_thread.daemon = True  # Thread exits when program exits
capture_thread.start()

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
    finally:
        picam2.stop() #ensure camera is stopped on exit.