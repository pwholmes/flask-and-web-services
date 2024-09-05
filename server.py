'''This module is the Flask server-side component of an Emotion Detection project'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''Render the main application page'''
    return render_template("index.html")

@app.route("/emotionDetector")
def analyze_text():
    '''Analyze the text in the textToAnalyze attribute and display the results'''
    # Retrieve the text to analyze from the request URL and call the analysis function
    text = request.args.get('textToAnalyze')
    results = emotion_detector(text)

    # Retrieve the dominant emotion and then prune that entry from the dictionary
    dominant = results['dominant_emotion']
    del results['dominant_emotion']

    # Format the results as instructed
    if dominant is None:
        response_text = "Invalid text!  Please try again!"
    else:
        response_text = "For the given statement, the system response is "
        response_text += ', '.join(f"{key}: {value}" for key, value in results.items())
        response_text += f". The dominant emotion is <b>{dominant}</b>."

    return response_text

# Execute the Flask app and deploy it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
