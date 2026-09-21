# Emotion Detector

This project is a Flask-based web application that uses IBM Watson NLP Emotion Detection to analyze the emotions expressed in user-provided text.

## Features

- Detects anger, disgust, fear, joy, and sadness.
- Displays the dominant emotion.
- Handles invalid or empty input gracefully.
- Uses the EmotionDetection package with Flask.

## Project Structure

emotion-detector/
- EmotionDetection/
  - __init__.py
  - emotion_detection.py
- templates/
  - index.html
- server.py
- test_emotion_detection.py
- README.md

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install flask requests pylint
```

## Run the Application

```bash
python server.py
```

Open `http://127.0.0.1:5000` in your browser.

## Test

Run:

```bash
python test_emotion_detection.py
```

## Static Code Analysis

Run:

```bash
pylint EmotionDetection
```