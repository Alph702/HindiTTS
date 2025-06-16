from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        rate = request.form["rate"]
        pitch = request.form["pitch"]
        volume = request.form["volume"]
        voice = request.form["voice"]

        output_file = "voice.mp3"

        cmd = [
            "edge-tts",
            "--text", text,
            "--voice", voice,
            f"--rate={'+' if int(rate) >= 0 else ''}{rate}%",
            f"--pitch={'+' if int(pitch) >= 0 else ''}{pitch}Hz",
            f"--volume={'+' if int(volume) >= 0 else ''}{volume}%",
            "--write-media", output_file
        ]

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            return f"⚠️ Voice generation failed: {e}"

        if not os.path.exists(output_file):
            return "⚠️ Voice file not created. Check edge-tts installation."

        return send_file(output_file, as_attachment=True, download_name="hindi_voice.mp3")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


