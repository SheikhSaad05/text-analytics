import numpy as np
# from scipy.special import softmax
import re
import json
from summarizer import Summarizer
from pysentimiento.preprocessing import preprocess_tweet
import requests
# from deep_translator import (GoogleTranslator)
# from app.strategy.data_models import DataModels
from app.strategy.utilities import Utilities

# data_models = DataModels()
lang_dt = Utilities

model_summarizer = Summarizer()
# Class


class LiveSentiment:

    def __init__(self, text):
        """

        :param text:
        """
        self.text = text
        self.response = dict()

    def preprocess(self):
        self.text_cleaning()
        self.summarize_text()

    def text_cleaning(self):
        self.text = str(self.text)
        self.text = self.text.lower()
        self.text = preprocess_tweet(self.text)
        self.text = re.sub(r'@[A-Za-z0-9]+', '', self.text)  # removing @mentions
        self.text = re.sub(r'@[A-Za-zA-Z0-9]+', '', self.text)  # removing @mentions
        self.text = re.sub(r'@[A-Za-z]+', '', self.text)  # removing @mentions
        self.text = re.sub(r'@[-)]+', '', self.text)  # removing @mentions
        self.text = re.sub(r'#', '', self.text)  # removing '#' sign
        self.text = re.sub(r'RT[\s]+', '', self.text)  # removing RT
        self.text = re.sub(r'https?\/\/\S+', '', self.text)  # removing the hyper link
        self.text = re.sub(r'&[a-z;]+', '', self.text)  # removing '&gt;'
        self.text = re.sub(r'&\w+', '', self.text)
        self.text = re.sub(r'(:|;)+', '', self.text)
        self.text = preprocess_tweet(self.text)

    def summarize_text(self):
        tokens = self.text.split('.')
        if len(tokens) > 2:
            result = model_summarizer(self.text, min_length=60, num_sentences=1)
            sum_text = ''.join(result)
            self.text = sum_text

    def get_sentiments(self):
        # encoded_input_s = data_models.tokenizer(self.text, return_tensors='pt', truncation=True)
        # # print(encoded_input_s)
        # output_s = data_models.model_s(**encoded_input_s)
        # scores_s = output_s[0][0].detach().numpy()
        # scores_s = softmax(scores_s)
        # # Print labels and scores
        # ranking_s = np.argsort(scores_s)
        # ranking_s = ranking_s[::-1]
        # predict_s = dict()
        # for i in range(scores_s.shape[0]):
        #     l = data_models.config.id2label[ranking_s[i]]
        #     s = scores_s[ranking_s[i]]
        #     # predict_s[l] = int(s * 100)
        #     predict_s[l] = round(float(s),2)
            # print(f"{i + 1}) {l} {np.round(float(s), 4)}")
        try:
            predict_s = requests.get('http://localhost:5010/sentiments?text={}'.format(self.text))
        except:
            predict_s = requests.get('http://sentiment:5010/sentiments?text={}'.format(self.text))

        predict_s = predict_s.json()
        self.response["sentiments"] = dict(predict_s)

    def get_emotions(self):
        # encoded_input_e = data_models.tokenizer_emo(self.text, return_tensors='pt', truncation=True)
        # # print(encoded_input_e)
        # output_e = data_models.model_e(**encoded_input_e)
        # scores_e = output_e[0][0].detach().numpy()
        # scores_e = softmax(scores_e)
        # # Print labels and scores
        # ranking_e = np.argsort(scores_e)
        # ranking_e = ranking_e[::-1]
        # predict_e = dict()
        # for i in range(scores_e.shape[0]):
        #     l = data_models.config_emo.id2label[ranking_e[i]]
        #     s = scores_e[ranking_e[i]]
        #     # predict_e[l] = int(s * 100)
        #     predict_e[l] = round(float(s),2)
        #     # print(f"{i + 1}) {l} {np.round(float(s), 4)}")
        try:
            predict_e = requests.get('http://localhost:5011/emotions?text={}'.format(self.text))
        except:
            predict_e = requests.get('http://emotion:5011/emotions?text={}'.format(self.text))

        predict_e = predict_e.json()
        self.response["emotions"] = dict(predict_e)

    def get_response(self):
        return self.response


if __name__ == '__main__':
    text = "First though, it’s important to keep in mind that responding to negative feedback is wrapped up in your strategy for managing the overall customer experience. We’ve gone into more detail here on the steps you can take to manage the customer experience, but it’s important to bear in mind how useful negative feedback can be in helping to understand your customers."
    obj = LiveSentiment(text)
    obj.preprocess()
    obj.get_sentiments()
    obj.get_emotions()
