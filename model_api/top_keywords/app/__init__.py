from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask import Flask
import yake

app = Flask(__name__)
CORS(app)

print('keywords model')
try:
    lang = 'en'
    n_gram = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    kw_extractor = yake.KeywordExtractor(lan=lang, n=n_gram, dedupLim=deduplication_threshold,
                                         top=numOfKeywords,
                                         features=None)
except:
    lang = 'en'
    n_gram = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    kw_extractor = yake.KeywordExtractor(lan=lang, n=n_gram, dedupLim=deduplication_threshold,
                                         top=numOfKeywords,
                                         features=None)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Keywords Model, is up and Running !"


@app.route('/keywords', methods=['GET'])
def predictions():
    text = request.args['text']
    keywords = kw_extractor.extract_keywords(text)
    keywords = jsonify({'keywords': keywords})

    return keywords
