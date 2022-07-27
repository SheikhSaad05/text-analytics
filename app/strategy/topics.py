import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions

# from app.strategy.data_models import Topics
# from transformers import TextClassificationPipeline
import requests


# topic_model = Topics()


# class TopicExtraction:
#     def __init__(self, text):
#         self.text = text
#         self.response = dict()
#
#     def topic_extraction(self):
#         # nlp = TextClassificationPipeline(model=topic_model.Model_topics, tokenizer=topic_model.tokenizer_topics)
#         #
#         # output = nlp(self.text, truncation=True)
#         # output_topic = topic_model.Model_topics(**encoded_input_topic)
#         # try:
#         #     output = requests.get('http://localhost:5013/topics?text={}'.format(self.text))
#         # except:
#         #     output = requests.get('http://topic:5013/topics?text={}'.format(self.text))
#
#         # output = output.json()
#         # output = output.get('topics')
#         # self.response['topics'] = output
#
#     def get_response(self):
#         print(self.response)
#         return self.response

class ConceptExtraction:
    def __init__(self, text):
        self.text = text
        self.concepts = dict()

        authenticator = IAMAuthenticator('ZewhCVLZM3z9lkDMCLvzzNtnWy0-Qk9HaRPwCAzCZ3no')
        self.nlu = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=authenticator
        )
        self.nlu.set_service_url(
            'https://api.jp-tok.natural-language-understanding.watson.cloud.ibm.com/instances/eda3eeee-31bf-457f-972b-65c5ff80b046')

    def get_concepts(self):
        response = self.nlu.analyze(
            text=self.text,
            features=Features(concepts=ConceptsOptions(limit=4))).get_result()

        print(json.dumps(response, indent=2))
        concepts = response.get("concepts", [])

        self.concepts['concepts'] = concepts

    def get_response(self):
        return self.concepts


if __name__ == '__main__':
    text = 'if you’re a skilled engineer with a DevOps mindset who has experience building CI/CD pipelines and is willing to learn and work with tools like Kubernetes and GCP cloud, then you will be happy to know that we’re looking for you to join our trivago team as a Site Reliability Engineer.'
    obj = ConceptExtraction(text)
    obj.get_concepts()
    obj.get_response()
