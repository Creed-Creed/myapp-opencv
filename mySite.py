from flask import Flask, render_template, Response
from cv2 import cv2


app = Flask(__name__)

@app.route('/')
def camera():
    return render_template('camera.html')

def get_frame():
    cam = cv2.VideoCapture(0)
    c = 0

    while 1:
        ret, img=cam.read()
        imgencode=cv2.imencode('.jpg', img)[1]
        stringData = imgencode.tostring()

        yield (b'--frame\r\n'
        b'Content-Type: Text/plain\r\n\r\n' + stringData+b'\r\n')

@app.route('/video_stream')
def video_stream():
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()
