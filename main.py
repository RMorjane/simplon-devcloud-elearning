from elearning import MyElearning
from flask import Flask, request, render_template, jsonify
import logging
import json

logging.basicConfig(filename='logs.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_video():
    learning = MyElearning()
    learning.set_logger()
    learning.connect()
    learning.read_videos()
    a = learning.list_videos
    return render_template("index.html",video = a)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)