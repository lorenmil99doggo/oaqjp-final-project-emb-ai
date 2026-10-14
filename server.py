"""
Emotion Detection Server
This module provides a Flask web application for detecting emotions
present in text submitted via a web interface or a query string.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Renders the application's main page."""
    return render_template("index.html")

#emotion detector call
@app.route("/emotionDetector")
def emot_detector():
    """It receives the text from the query string, analyzes it using emotion_detector,
    and returns the emotion scores along with the dominant emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    #emotion_detector calling & dictionary results
    response = emotion_detector(text_to_analyze)
    #analysis
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    #error handling
    return (
        f"'anger': {response['anger']},"
        f"'disgust': {response['disgust']},"
        f"'joy': {response['joy']},"
        f"'sadness': {response['sadness']},"
        f"'Dominant emotion': {response['dominant_emotion']},"
    )
    #formatted response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
