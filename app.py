from flask import Flask, jsonify

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/videos")
def get_videos():
    videos = [
        {
            "title": "1st Episode",
            "url": "https://rumble.com/embed/v64mgw1/?pub=y5av6"
        },
        {
            "title": "2nd Episode",
            "url": "https://rumble.com/embed/v64n0qm/?pub=y5av6"
        },
        {
            "title": "3rd Episode",
            "url": "https://rumble.com/embed/v64n0qm/?pub=y5av6"
        }
    ]
    return jsonify(videos)

