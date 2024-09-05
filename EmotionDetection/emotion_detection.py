import requests
import json

def emotion_detector(text_to_analyse):
    '''Call IBM's Emotion Predictor service and return the results'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Extract the desired data from the response (i.e., the list of emotions and their scores)
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 400:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    else:
        json_response = json.loads(response.text)
        emotions = json_response['emotionPredictions'][0]['emotion']

        # Find the emotion with the highest score and add an entry to the dictionary to note it
        high_emotion = None
        high_score = 0
        for emotion,score in emotions.items():
            if score > high_score:
                high_score = score
                high_emotion = emotion
        emotions["dominant_emotion"] = high_emotion

    return emotions
