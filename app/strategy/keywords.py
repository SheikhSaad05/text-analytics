# from app.strategy.data_models import KeywordsModels
# import json
import requests


# kw_models = KeywordsModels()


class KeywordExtraction:
    def __init__(self, text):
        self.text = text
        self.response = dict()

    def detect_keywords(self):
        """
        Return keywords of the paragraph
        :return:
        """
        # keywords = kw_models.kw_extractor.extract_keywords(self.text)
        try:
            keywords = requests.get('http://localhost:5014/keywords?text={}'.format(self.text))
        except:
            keywords = requests.get('http://keyword:5014/keywords?text={}'.format(self.text))

        keywords = keywords.json()
        keywords = keywords.get('keywords')

        self.response["keyword"] = keywords

    def get_response(self):
        return self.response


if __name__ == '__main__':
    text = "Horrible customer service. Receptionist is extremly rude. I have called regarding a roofing report weekly for over a month and never received the report. I asked to hold to speak with a manager or the owner and was told by the receptionsit that she didn't control."
    obj_1 = KeywordExtraction(text)
    obj_1.detect_keywords()
