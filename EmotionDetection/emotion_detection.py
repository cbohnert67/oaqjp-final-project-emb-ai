import requests
import json

def emotion_detector(text_to_analyse):
    """
    Envoie une requête à l'API Watson pour détecter les émotions dans un texte.

    :param text_to_analyse: Texte à analyser.
    :return: Dictionnaire contenant les émotions détectées ou un message d'erreur.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Vérifie si la requête a réussi
        response_dict = response.json()['emotionPredictions'][0]['emotion']  # Retourne la réponse de l'API en JSON
        emotions = {
            'anger': response_dict.get('anger', 0),
            'disgust': response_dict.get('disgust', 0),
            'fear': response_dict.get('fear', 0),
            'joy': response_dict.get('joy', 0),
            'sadness': response_dict.get('sadness', 0)
            }
         # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
    
        return emotions
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


