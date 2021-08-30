from elearning import MyElearning
from flask import Flask, request, render_template, jsonify
import logging
import json

logging.basicConfig(filename='logs.log',level=logging.DEBUG)

learning = MyElearning()
learning.set_logger()
learning.connect()

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_video():
    name = request.args.get("video")
    if name == None:
        learning.read_videos()
    else:
        learning.find_videos({
            "video_name": str(name)
        })
    a = learning.list_videos
    return render_template("index.html",video = a)

@app.route('/video/<video_id>',methods=['GET'])
def video_page(video_id):
    learning.find_videos({
        "video_id": int(video_id)
    }) 
    list_videos = learning.list_videos
    a = list_videos[0]
    learning.read_videos()
    b = learning.list_videos
    print("-----------")
    return render_template("see_video.html", video = a, video_all = b)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)
