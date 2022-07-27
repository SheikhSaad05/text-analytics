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

print("Sentiment Model")
try:
    MODEL_Sentiment = "/app/finiteautomata/bertweet-base-sentiment-analysis"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_Sentiment)
    config = AutoConfig.from_pretrained(MODEL_Sentiment)

    model_s = AutoModelForSequenceClassification.from_pretrained(MODEL_Sentiment)
    # model_s.save_pretrained(MODEL_Sentiment)
    # tokenizer.save_pretrained(MODEL_Sentiment)

except:
    # PT_Sentiment
    MODEL_Sentiment = "finiteautomata/bertweet-base-sentiment-analysis"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_Sentiment)
    config = AutoConfig.from_pretrained(MODEL_Sentiment)

    model_s = AutoModelForSequenceClassification.from_pretrained(MODEL_Sentiment)
    model_s.save_pretrained(MODEL_Sentiment)
    tokenizer.save_pretrained(MODEL_Sentiment)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Sentiment Model, is up and Running !"


@app.route('/sentiments', methods=['GET'])
def predictions():
    text = request.args['text']
    """
    variable text is initialize with input text from api/
    """
    encoded_input_s = tokenizer(text, return_tensors='pt', truncation=True)
    # print(encoded_input_s)
    output_s = model_s(**encoded_input_s)
    scores_s = output_s[0][0].detach().numpy()
    scores_s = softmax(scores_s)
    # Print labels and scores
    ranking_s = np.argsort(scores_s)
    ranking_s = ranking_s[::-1]
    predict_s = dict()
    for i in range(scores_s.shape[0]):
        l = config.id2label[ranking_s[i]]
        s = scores_s[ranking_s[i]]
        # predict_s[l] = int(s * 100)
        predict_s[l] = round(float(s), 2)

    return jsonify(predict_s)
