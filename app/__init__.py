# import torch
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required

import readtime

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from app.strategy.prediction import LiveSentiment
from app.strategy.keywords import KeywordExtraction
# from app.strategy.title_gen import TitleGenerator
from app.strategy.utilities import Utilities
# from app.strategy.entity_extraction import EntityExtraction
from app.strategy.questions import QuestionExtraction
# from app.strategy.topics import TopicExtraction
from app.strategy.topics import ConceptExtraction

# from summarizer import Summarizer
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from transformers import AutoModelForTokenClassification, AutoTokenizer
# from transformers import AutoModelForSequenceClassification, AutoTokenizer
#
# from transformers import T5Config, T5ForConditionalGeneration, T5Tokenizer
# from transformers import TextClassificationPipeline
# from transformers import AutoConfig

import os

sentry_sdk.init(
    dsn="https://e7a9df6aab2d4d22a9074d7a5680e2d8@sentry-onpremise.contentstudio.io/49",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

util_obj = Utilities()


app = Flask(__name__)
CORS(app)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_IDENTITY_CLAIM'] = "sub"
app.config['JWT_SECRET_KEY'] = '5A9x0UTD4JLGt4j0Timd7uv48n3uUk9a'
app.config['JWT_DECODE_ALGORITHMS'] = ['HS256']
jwt = JWTManager(app)


@app.route('/debug-sentry', methods=['GET', 'POST'])
def trigger_error():
    try:
        division_by_zero = 1 / 0
    except Exception as ex:
        sentry_sdk.capture_exception(ex)
    return "ok"


@app.route('/', methods=['GET'])
def home():
    return "Welcome to SEO"


@app.route('/cwd', methods=['GET'])
def cwd():
    res = str(os.getcwd())
    return res


@app.route('/isPath', methods=['GET'])
def isPath():
    text = request.args['text']
    res = str(os.path.isdir(text))
    return res


# @app.route('/loadModel', methods=['GET'])
# def loadModel():
#     text = request.args['text']
#     MODEL_Sentiment = text
#     tokenizer = AutoTokenizer.from_pretrained(MODEL_Sentiment)
#     config = AutoConfig.from_pretrained(MODEL_Sentiment)
#     # PT_Sentiment
#     model_s = AutoModelForSequenceClassification.from_pretrained(MODEL_Sentiment)
#     model_s.save_pretrained(MODEL_Sentiment)
#     tokenizer.save_pretrained(MODEL_Sentiment)
#     return "success"

# @app.route('/loadModelT', methods=['GET'])
# def loadModelT():
#
#     Model_topics = AutoModelForSequenceClassification.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     tokenizer_topics = AutoTokenizer.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     # PT_Topics
#     Model_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     tokenizer_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#     return "success"

# @app.route('/loadModelQ', methods=['GET'])
# def loadModelQ():
#
#     model_path_q = "allenai/t5-small-squad2-question-generation"
#     Model_questions = T5ForConditionalGeneration.from_pretrained(model_path_q)
#     tokenizer_questions = T5Tokenizer.from_pretrained(model_path_q)
#
#     # PT_Questions
#     Model_questions.save_pretrained(model_path_q)
#     tokenizer_questions.save_pretrained(model_path_q)
#     return "success"


@app.route('/predictions', methods=['GET'])
def predictions():
    text = request.args['text']
    """
    variable text is initialize with input text from api/
    """
    response = dict()
    response['text'] = text
    response['char_length'] = len(text)

    lang = util_obj.detect_language(text)
    text = util_obj.translate(lang, text)

    try:
        obj = LiveSentiment(text)
        obj.preprocess()
    except Exception as ex:
        pass
    try:
        obj.get_sentiments()
    except Exception as ex:
        pass
    try:
        obj.get_emotions()
    except Exception as ex:
        pass

    try:
        obj_1 = KeywordExtraction(text)
        obj_1.detect_keywords()
    except Exception as ex:
        pass

    se_res = obj.get_response()
    # te_res = obj_2.get_response()

    summarize_text = obj.text
    # titles = te_res.get('title')
    sentiments = se_res.get('sentiments')
    emotions = se_res.get('emotions')
    keywords = obj_1.get_response().get('keyword')

    read_time = readtime.of_text(text)

    if lang != 'en':
        summarize_text = util_obj.convert_language(summarize_text, source_lang='en', target_lang=lang)
        keywords = [[util_obj.convert_language(keyword_[0], source_lang='en', target_lang=lang), keyword_[1]]
                    for keyword_ in keywords]

    response['readtime'] = read_time.seconds
    response['summarize_text'] = summarize_text
    response['sentiments'] = sentiments
    response['emotions'] = emotions
    response['keywords'] = keywords

    result = jsonify(response)
    return result


@app.route('/question', methods=['GET'])
def question():
    text = request.args['text']
    response_q = dict()

    lang = util_obj.detect_language(text)
    text = util_obj.translate(lang, text)

    try:
        obj_q = QuestionExtraction(text)
        obj_q.question_extraction()

    except Exception as ex:
        print("Some thing went wrong in Questions")

    question_ = obj_q.get_response().get('questions')

    if lang != 'en':
        question_ = [util_obj.convert_language(x, source_lang='en', target_lang=lang) for x in question_]

    response_q['questions'] = question_
    result_q = jsonify(response_q)

    return result_q


@app.route('/topics', methods=['GET'])
def topics():
    text = request.args['text']
    response_t = dict()

    lang = util_obj.detect_language(text)
    text = util_obj.translate(lang, text)

    # try:
    #     obj_t = LiveSentiment(text)
    #     obj_t.text_cleaning()
    # except Exception as ex:
    #     pass
    try:
        obj_t = ConceptExtraction(text)
        obj_t.get_concepts()

    except Exception as ex:
        print("Some thing went wrong in Topics")

    concepts_ = obj_t.get_response().get('concepts')

    if lang != 'en':
        concepts_ = [util_obj.translate(lang, x) for x in concepts_]
        # topics_ = [util_obj.convert_language(x, source_lang='en', target_lang=lang) for x in topics_]

    response_t['concepts'] = concepts_
    result_1 = jsonify(response_t)

    return result_1
