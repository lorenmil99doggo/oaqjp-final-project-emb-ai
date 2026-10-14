#import import dependencies
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

#template
@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emot_detector():
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
