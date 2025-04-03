from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Get the text from the request
    data = request.get_json()
    text_to_analyse = data.get('text', '')

    # Call the emotion detector function
    emotions = emotion_detector(text_to_analyse)

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