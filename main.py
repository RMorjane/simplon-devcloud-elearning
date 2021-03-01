from elearning import MyElearning
from flask import Flask, request, render_template, jsonify
import logging
import json
app = Flask(__name__)

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

learning = MyElearning()
learning.set_logger()
learning.connect() 

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
   
    
@app.route('/', methods=['GET'])
def get_video():
    learning = MyElearning()
    learning.set_logger()
    learning.connect()    
    learning.read_videos()
    a = learning.list_videos
    return render_template("indexmorjane.html", video = a)

@app.route('/index', methods=['GET'])
def get_index():
    learning = MyElearning()
    learning.set_logger()
    learning.connect()    
    learning.read_videos()
    a = learning.list_videos
    return render_template("testasup.html", video = a)


@app.route('/css', methods=['GET'])
def getcss():
    learning = MyElearning()
    learning.set_logger()
    learning.connect()    
    learning.read_videos()
    a = learning.list_videos
    return render_template("css.html", video = a)

@app.route('/csscategorie', methods=['GET'])
def categoriecss():
    learning = MyElearning()
    learning.set_logger()
    learning.connect()    
    learning.read_vcategories()
    a = learning.list_vcategories
    print("----------")
    print(a)
    return render_template("categorie.html", category = a)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)