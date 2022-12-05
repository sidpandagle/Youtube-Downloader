
import sys
import os
from pytube import YouTube
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/download_audio", methods=["GET","POST"])
def download_video():
    try:
        url = request.get_json(force=True)['url']
        yt = YouTube(url)
        videos = yt.streams.filter(only_audio=True)
        # Check Format provided in vidArr
        # vidArr = list(enumerate(videos))
        # for x in vidArr:
        #     print(x) 
        # fname = videos[4].download().split("//")[-1]
        fname = videos[4].download(filename=yt.title+'.mp3')
        return send_file(fname, as_attachment=True)
    except:
        return "Video download failed!"