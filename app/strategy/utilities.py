from deep_translator import (GoogleTranslator)
import requests
import json

domain_id = "ADFF849040"


class Utilities:
    def __init__(self):
        pass

    def detect_language(self, text_):
        """
        :param text_: Original text is passed here to detect the language
        :return: It returns the language of passed text

        """
        response = requests.post("http://language-classification.contentstudio.io/classify",
                                 data={"text": text_, "ids": domain_id},
                                 headers={'fasttext': 'contentstudio'})
        lang = json.loads(response.text)[0].get('label')
        # print(lang)
        return lang

    def translate(self, lang, text_):
        """
        :param lang: In Case if language of text is not english we passed the language
        :param text_: Original text is passed here to be translated
        :return: Translated text is returned for further analysis
        """
        if lang.lower() != "en":
            return self.convert_language(text_, source_lang=lang, target_lang='en')
        return text_

    def convert_language(self, text_, source_lang, target_lang):
        translated_language = GoogleTranslator(source=source_lang, target=target_lang)
        return translated_language.translate(text=text_)
        # print(self.text)

# if __name__ == '__main__':
#     text = "."
#     obj_l = Utilities(text)
#     obj_l.detect_language()
#     obj_l.translate()
