"""IBM Watson Emotion Detection module."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)


def emotion_detector(text_to_analyze):
    """Analyze emotions using IBM Watson NLP."""

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code == 400:
            return None

        response.raise_for_status()

        emotions = response.json()["emotionPredictions"][0]["emotion"]

        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant
        }

    except requests.exceptions.RequestException:
        return None
    