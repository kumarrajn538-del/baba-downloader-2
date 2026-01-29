from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

def get_video_link(url):
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('url', None)
    except Exception as e:
        return None

@app.route('/')
def home():
    return render_template('downloader.html')

@app.route('/download', methods=['POST'])
def download():
    user_url = request.json.get('url')
    video_link = get_video_link(user_url)
    if video_link:
        return jsonify({"success": True, "link": video_link})
    return jsonify({"success": False, "error": "Bhai, link sahi nahi hai!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
