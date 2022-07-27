# from summarizer import Summarizer
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from transformers import AutoModelForTokenClassification, AutoTokenizer
# from transformers import AutoModelForSequenceClassification, AutoTokenizer
#
# from transformers import T5Config, T5ForConditionalGeneration, T5Tokenizer
# from transformers import TextClassificationPipeline
# from transformers import AutoConfig
# import yake
#
#
# # # import tensorflow as tf
# #
# #
# class DataModels:
#
#     def __init__(self):
#         self.model_summarizer = Summarizer()
#
#         print("Sentiment Model")
#
#         # Sentiment_Model_Initializer
#         try:
#             self.MODEL_Sentiment = "/app/finiteautomata/bertweet-base-sentiment-analysis"
#             self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_Sentiment)
#             self.config = AutoConfig.from_pretrained(self.MODEL_Sentiment)
#
#         except:
#             # PT_Sentiment
#             self.MODEL_Sentiment = "finiteautomata/bertweet-base-sentiment-analysis"
#             self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL_Sentiment)
#             self.config = AutoConfig.from_pretrained(self.MODEL_Sentiment)
#
#         self.model_s = AutoModelForSequenceClassification.from_pretrained(self.MODEL_Sentiment)
#         self.model_s.save_pretrained(self.MODEL_Sentiment)
#         self.tokenizer.save_pretrained(self.MODEL_Sentiment)
#
#         print ("Emotion Model")
#         # Emotion_Model_Initializer
#         try:
#             self.MODEL_Emotion = "/app/nateraw/bert-base-uncased-emotion"
#             self.tokenizer_emo = AutoTokenizer.from_pretrained(self.MODEL_Emotion)
#             self.config_emo = AutoConfig.from_pretrained(self.MODEL_Emotion)
#         except:
#             self.MODEL_Emotion = "nateraw/bert-base-uncased-emotion"
#             self.tokenizer_emo = AutoTokenizer.from_pretrained(self.MODEL_Emotion)
#             self.config_emo = AutoConfig.from_pretrained(self.MODEL_Emotion)
#         # PT_Emotion
#         self.model_e = AutoModelForSequenceClassification.from_pretrained(self.MODEL_Emotion)
#         self.model_e.save_pretrained(self.MODEL_Emotion)
#         self.tokenizer_emo.save_pretrained(self.MODEL_Emotion)
#
#
# #
# #
# class KeywordsModels:
#     def __init__(self):
#         self.lang = 'en'
#         self.n_gram = 3
#         self.deduplication_threshold = 0.9
#         self.numOfKeywords = 20
#         self.kw_extractor = yake.KeywordExtractor(lan=self.lang, n=self.n_gram, dedupLim=self.deduplication_threshold,
#                                                   top=self.numOfKeywords,
#                                                   features=None)
#
#
# #
# # class TitleModels:
# #     def __init__(self):
# #         # Title Generator model initializer
# #
# #         self.Model_title = "Callidior/bert2bert-base-arxiv-titlegen"
# #         self.tokenizer_t = AutoTokenizer.from_pretrained(self.Model_title)
# #         self.model_t = AutoModelForSeq2SeqLM.from_pretrained(self.Model_title)
# #         self.config_t = AutoConfig.from_pretrained(self.Model_title)
# #
# #         # PT_Title
# #
# #         self.model_t.save_pretrained(self.Model_title)
# #         self.tokenizer_t.save_pretrained(self.Model_title)
# #
# #
# # class Entities:
# #     def __init__(self):
# #         print("entities model")
# #         self.model_path = "Emanuel/autonlp-pos-tag-bosque"
# #         self.Model_Entities = AutoModelForTokenClassification.from_pretrained(self.model_path)
# #         self.tokenizer_entities = AutoTokenizer.from_pretrained(self.model_path)
# #         # PT_Entities
# #         self.Model_Entities.save_pretrained(self.model_path)
# #         self.tokenizer_entities.save_pretrained(self.model_path)
# #
# #
# class Topics:
#     def __init__(self):
#         print('topic model')
#         try:
#             # model_name = 'lincoln/flaubert-mlsum-topic-classification'
#             self.Model_topics = AutoModelForSequenceClassification.from_pretrained('/app/lincoln/flaubert-mlsum-topic-classification')
#             self.tokenizer_topics = AutoTokenizer.from_pretrained('/app/lincoln/flaubert-mlsum-topic-classification')
#         except:
#             self.Model_topics = AutoModelForSequenceClassification.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#             self.tokenizer_topics = AutoTokenizer.from_pretrained('lincoln/flaubert-mlsum-topic-classification')
#
#         # PT_Topics
#         self.Model_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
#         self.tokenizer_topics.save_pretrained('lincoln/flaubert-mlsum-topic-classification')
# #
# #
# class Questions:
#     def __init__(self):
#         print('question model')
#         try:
#
#             self.model_path_q = "/app/allenai/t5-small-squad2-question-generation"
#             self.Model_questions = T5ForConditionalGeneration.from_pretrained(self.model_path_q)
#             self.tokenizer_questions = T5Tokenizer.from_pretrained(self.model_path_q)
#
#         except:
#             self.model_path_q = "allenai/t5-small-squad2-question-generation"
#             self.Model_questions = T5ForConditionalGeneration.from_pretrained(self.model_path_q)
#             self.tokenizer_questions = T5Tokenizer.from_pretrained(self.model_path_q)
#
#         # PT_Questions
#         self.Model_questions.save_pretrained(self.model_path_q)
#         self.tokenizer_questions.save_pretrained(self.model_path_q)
