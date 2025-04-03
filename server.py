"""
This module implements a Flask application for detecting emotions in text.
It provides an endpoint '/emotionDetector' that accepts POST requests with text input
and returns the detected emotions in a formatted response.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detects emotions from the provided text input.

    This function handles POST requests to the '/emotionDetector' endpoint.
    It retrieves the text from the request, processes it to detect emotions,
    and returns a formatted response with the detected emotions.

    Returns:
        str: A formatted string with the detected emotions or an error message.
    """
    # Get the text from the request
    data = request.get_json()
    text_to_analyse = data.get('text', '')

    # Check for blank input
    if not text_to_analyse.strip():
        # Return a 400 status code for blank input
        emotions = emotion_detector('', 400)
    else:
        emotions = emotion_detector(text_to_analyse, 200)

    # Check if the dominant emotion is None
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again.", 400

    # Format the response
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    # Return the formatted response
    return response_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
