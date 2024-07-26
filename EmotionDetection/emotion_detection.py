import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    response = requests.post(url, json = myobj, headers=header) 
    responsejson = json.loads(response.text)
    
    if response.status_code == 200:

        formatted_response = {
            'anger':responsejson['emotionPredictions'][0]['emotion']['anger'],
            'disgust':responsejson['emotionPredictions'][0]['emotion']['disgust'],
            'fear':responsejson['emotionPredictions'][0]['emotion']['fear'],
            'joy':responsejson['emotionPredictions'][0]['emotion']['joy'],
            'sadness':responsejson['emotionPredictions'][0]['emotion']['sadness'],
            'dominant_emotion': max(responsejson['emotionPredictions'][0]['emotion'], key=responsejson['emotionPredictions'][0]['emotion'].get)
        }
    elif response.status_code == 400: 
        formatted_response = {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,
        'dominant_emotion': None
        }
    return formatted_response