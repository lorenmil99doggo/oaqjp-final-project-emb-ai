import requests
import json

def emotion_detector(text_to_analyze):
    #no text error
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    #URL watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #What NLP model to use
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #text fomrat for Watson
    obj = { "raw_document": { "text": text_to_analyze } }
    # request
    response = requests.post(url, json=obj, headers=headers)
    #server response 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    #change response to JSON
    formatted_response = json.loads(response.text)
    #making  a list of emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    #taking the most probable emotion
    dominant_emotion = max(emotions, key=emotions.get)
    #emotions score
    emotions['dominant_emotion'] = dominant_emotion
    #response
    return emotions