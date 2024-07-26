"""
This is the final project in which I developed a little web app with AI
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector", template_folder='/home/project/final_project/templates')

@app.route('/emotionDetector')
def emo_detector():
    """Funtion to dect the emotion given in a messag"""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if anger is None:
        return " Invalid text! Please try again!."

    return f"For the given statement, the system response is \
    'anger': {anger}, 'disgust': {disgust}, 'fear':{fear}, \
    'joy': {joy}, 'sadness': {sadness}., the dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    '''Funtion to render the main page of the web app'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
