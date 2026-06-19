"""
Flask server for Emotion Detection project.
Provides routes for emotion analysis and rendering the index page.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for emotion detection
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
   This function return emotion with given input
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Call your emotion_detector function
    result = emotion_detector(text_to_analyze)

    if not text_to_analyze:
        return jsonify(result), 400

    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return jsonify(result), 200

@app.route("/")
def render_html():
    """
    Render the index.html template for the web interface.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
