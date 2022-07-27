from transformers import T5Config, T5ForConditionalGeneration, T5Tokenizer
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)

print('question model')
try:
    model_path_q = "/app/allenai/t5-small-squad2-question-generation"
    Model_questions = T5ForConditionalGeneration.from_pretrained(model_path_q)
    tokenizer_questions = T5Tokenizer.from_pretrained(model_path_q)

    # Model_questions.save_pretrained(model_path_q)
    # tokenizer_questions.save_pretrained(model_path_q)

except:
    model_path_q = "allenai/t5-small-squad2-question-generation"
    Model_questions = T5ForConditionalGeneration.from_pretrained(model_path_q)
    tokenizer_questions = T5Tokenizer.from_pretrained(model_path_q)

    Model_questions.save_pretrained(model_path_q)
    tokenizer_questions.save_pretrained(model_path_q)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to Question Model, is up and Running !"


@app.route('/questions', methods=['GET'])
def predictions():
    text = request.args['text']
    input_ids = tokenizer_questions.encode(text, return_tensors="pt")
    res = Model_questions.generate(input_ids, do_sample=True, num_return_sequences=3)
    output = tokenizer_questions.batch_decode(res, skip_special_tokens=True)

    return jsonify({"questions": output})
