from flask import render_template, Response
from app import app
from app.forms import EmailForm
from app.capture import gen_frame

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")

@app.route("/video_feed")
def video_feed():
    return Response(gen_frame(), mimetype="multipart/x-mixed-replace; boundary=frame")