# Repository for final project

project name = final_Project

# Final Project - Emotion Detection Web App

This project is part of the Coursera course **Python Project for AI Application Development**.  
It demonstrates how to build and deploy a Flask-based web application that performs **emotion detection** using IBM Watson NLP services.


- Flask backend (`server.py`) with routes:
  - `/emotionDetector` → analyzes text input and returns emotions in JSON.
  - `/` → renders the web interface (`index.html`).
- Emotion detection logic implemented in `EmotionDetection/emotion_detection.py`.
- Frontend (`index.html` + `static/mywebscript.js`) for user interaction.
- Error handling:
  - Returns `400` with `None` values when input is blank.
  - Returns a friendly message when `dominant_emotion` is `None`.

## 📂 Project Structure
├── EmotionDetection/
│   ├── init.py
│   ├── emotion_detection.py
│   └── server.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
└── README.md


## ⚙️ Setup & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/surajk236789/final_project_clone/tree/fianl_project_dev

pip install flask requests
python3 EmotionDetection/server.py



