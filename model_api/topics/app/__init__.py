# from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
# from flask import Flask, request, jsonify, abort
# from flask_cors import CORS
# from flask import Flask
#
# app = Flask(__name__)
# CORS(app)
#
# print('topic model')
# try:
#     # model_name = 'lincoln/flaubert-mlsum-topic-classification'
#     Model_topics = AutoModelForSequenceClassification.from_pretrained('/app/lincoln/flaubert-mlsum-topic-classification', from_tf=False)
#     tokenizer_topics = AutoTokenizer.from_pretrained('/app/lincoln/flaubert-mlsum-topic-classification')
#
#     # PT_Topics
#     # Model_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     # tokenizer_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
# except:
#     Model_topics = AutoModelForSequenceClassification.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     tokenizer_topics = AutoTokenizer.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#
#     # PT_Topics
#     Model_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     tokenizer_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#
#
# @app.route('/', methods=['GET'])
# def home():
#     return "Welcome to Topics Model, is up and Running !"
#
#
# @app.route('/topics', methods=['GET'])
# def predictions():
#     text = request.args['text']
#     nlp = TextClassificationPipeline(model=Model_topics, tokenizer=tokenizer_topics)
#
#     output = nlp(text, truncation=True)
#     output = jsonify({'topics': output})
#
#     return output
