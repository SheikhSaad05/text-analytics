from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import AutoConfig
from scipy.special import softmax
import numpy as np

app = Flask(__name__)
CORS(app)

print("Emotion Model")
# Emotion_Model_Initializer
try:
    MODEL_Emotion = "/app/nateraw/bert-base-uncased-emotion"
    tokenizer_emo = AutoTokenizer.from_pretrained(MODEL_Emotion)
    config_emo = AutoConfig.from_pretrained(MODEL_Emotion)

    # PT_Emotion
    model_e = AutoModelForSequenceClassification.from_pretrained(MODEL_Emotion)
    # model_e.save_pretrained(MODEL_Emotion)
    # tokenizer_emo.save_pretrained(MODEL_Emotion)

except:
    MODEL_Emotion = "nateraw/bert-base-uncased-emotion"
    tokenizer_emo = AutoTokenizer.from_pretrained(MODEL_Emotion)
    config_emo = AutoConfig.from_pretrained(MODEL_Emotion)

    # PT_Emotion
    model_e = AutoModelForSequenceClassification.from_pretrained(MODEL_Emotion)
    model_e.save_pretrained(MODEL_Emotion)
    tokenizer_emo.save_pretrained(MODEL_Emotion)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Emotion Model, is up and Running !"


@app.route('/emotions', methods=['GET'])
def predictions():
    text = request.args['text']
    """
    variable text is initialize with input text from api/
    """
    encoded_input_e = tokenizer_emo(text, return_tensors='pt', truncation=True)
    # print(encoded_input_e)
    output_e = model_e(**encoded_input_e)
    scores_e = output_e[0][0].detach().numpy()
    scores_e = softmax(scores_e)
    # Print labels and scores
    ranking_e = np.argsort(scores_e)
    ranking_e = ranking_e[::-1]
    predict_e = dict()
    for i in range(scores_e.shape[0]):
        l = config_emo.id2label[ranking_e[i]]
        s = scores_e[ranking_e[i]]
        # predict_e[l] = int(s * 100)
        predict_e[l] = round(float(s), 2)
        # print(f"{i + 1}) {l} {np.round(float(s), 4)}")

    return jsonify(predict_e)
