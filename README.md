# 🎤 Indie Hindi Voice Generator

Indie Hindi Voice Generator is a web application that allows users to generate and download Hindi text-to-speech (TTS) audio files using Microsoft's neural voices. The app is built with Flask and uses the `edge-tts` library for voice synthesis.

## 🌟 Features

- 🎙 Generate high-quality Hindi TTS audio.
- 🎚️ Customize speech rate, pitch, and volume.
- 🎵 Choose between male and female voices.
- 🎧 Download the generated audio as an MP3 file.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)
- `edge-tts` installed on your system

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HindiTTS.git
   cd HindiTTS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `edge-tts` is installed and accessible from the command line.

## 🛠️ Usage

1. Start the Flask server:
   ```bash
   python main.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter the Hindi text, adjust the rate, pitch, and volume, select a voice, and click "Generate & Download Voice" to download the MP3 file.

## 📂 Project Structure

```
HindiTTS/
├── templates/          # HTML templates for the web app
├── static/             # Static files (if any)
├── main.py             # Flask application
├── requirements.txt    # Python dependencies
├── .render.yaml        # Render deployment configuration
├── README.md           # Project documentation
```

## 🛠 Deployment

This project is configured for deployment on Render. To deploy:

1. Push your code to a Git repository.
2. Connect your repository to Render.
3. Render will automatically use the `.render.yaml` file to build and deploy your app.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## ❤️ Acknowledgments

- Built with Flask and `edge-tts`.
- Inspired by the need for high-quality Hindi TTS solutions.