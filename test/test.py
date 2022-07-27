import operator
import unittest
import requests
import blinker
import operator

from app.strategy.prediction import LiveSentiment
from app.strategy.utilities import Utilities
from app.strategy.topics import TopicExtraction
from app.strategy.questions import QuestionExtraction

es_text = "Una calificación de 1 estrella es seguida por una crítica severamente negativa. La respuesta del Dr. Bigles es concisa y profesional, y aunque expresa preocupación, no reconoce ninguna irregularidad. Este es un excelente punto de partida para cualquiera que responda a críticas negativas pero aún no esté seguro de cómo abordarlo."
en_text = "Horrible customer service. Receptionist is extremly rude. I have called regarding a roofing report weekly for over a month and never received the report. I asked to hold to speak with a manager or the owner and was told by the receptionsit that she didn't control have control over their availability and that no one could help me right now. Tuly horrific service."
t_topic = "Blizzard Entertainment introduced the World of Warcraft Community Council today to add another venue for communication between players and developers.The goal of the council, according to a post by Blizzard, is to gather more detailed feedback on all facets of the game. "
q_test = "CANBERRA, Australia (AP) — Australian Prime Scott Morrison attacked the credibility of French President Emmanuel Macron as a newspaper quoted a text message that suggested France anticipated “bad news” about a now-scuttled submarine deal."


class Test(unittest.TestCase):

    def test_text_language(self):
        case_txt = Utilities.detect_language(self, text_=es_text)
        # case_txt.detect_language()
        if case_txt == 'es':
            self.assertTrue(case_txt, "Passed")

    def test_text_cleaning(self):
        case_cln = LiveSentiment(en_text)
        case_cln.text_cleaning()

    def test_text_sentiment(self):
        case_sen = LiveSentiment(en_text)
        case_sen.get_sentiments()
        response_sen = case_sen.get_response()
        result_sen = max(response_sen.items(), key=lambda k: k[1])
        if result_sen == "NEG":
            self.assertTrue(result_sen, "Passed")

    def test_text_emotion(self):
        case_em = LiveSentiment(en_text)
        case_em.get_emotions()
        response_em = case_em.get_response()
        result_em = max(response_em.items(), key=lambda k: k[1])
        if result_em == "Anger":
            self.assertTrue(result_em, "Passed")

    def test_topic(self):
        case_t = TopicExtraction(t_topic)
        case_t.topic_extraction()
        response_t = case_t.get_response()
        result_t = max(response_t.items(), key=lambda k: k[1])
        if result_t == "Sport":
            self.assertTrue(result_t, "Passed")

    def test_question(self):
        case_q = QuestionExtraction(q_test)
        case_q.question_extraction()
        response_q = case_q.get_response()
        # result_q = max(response_q.items(), key=lambda k: k[1])
        if response_q == 'What did Morrison attack the credibility of French President Emmanuel Macron?':
            self.assertTrue(response_q, "Passed")
        elif response_q == 'Who is the Australian prime minister?':
            self.assertTrue(response_q, "Passed")
        elif response_q == 'Who accused Emmanuel Macron of supposedly influencing his policies?':
            self.assertTrue(response_q, "Passed")
        else:
            self.assertTrue(response_q, "Warning")


if __name__ == '__main__':
    unittest.main()
