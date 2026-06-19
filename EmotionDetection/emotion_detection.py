import requests
import json

def emotion_detector(text_to_analyze):
    URL = r'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Obj = { "raw_document": { "text": text_to_analyze } }
    if not text_to_analyze:
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        return result
    
    response = requests.post(url=URL, json = Obj, headers=Headers)
    final_response = json.loads(response.text)
    emotions = final_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions,key = emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    return emotions