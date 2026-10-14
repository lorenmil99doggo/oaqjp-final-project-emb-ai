import requests

def emotion_detector(text_to_analyze):
    #URL watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #What NLP model to use
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #text fomrat for Watson
    obj = { "raw_document": { "text": text_to_analyze } }
    # request
    response = requests.post(url, json=obj, headers=headers)
    #response
    return response.text