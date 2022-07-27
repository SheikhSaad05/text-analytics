# from app.strategy.data_models import TitleModels
# import numpy as np
# from scipy.special import softmax
#
# tl_model = TitleModels()
#
#
# class TitleGenerator:
#
#     def __init__(self, text):
#         self.text = text
#         self.response = dict()
#
#     def get_title(self):
#         encoded_input_t = tl_model.tokenizer_t(self.text, padding='longest', truncation=True,
#                                                return_tensors='pt').input_ids
#         # print(encoded_input_t)
#         # output_t = tl_model.model_t(**encoded_input_t)
#         output_t = tl_model.model_t.generate(encoded_input_t, do_sample=True, top_k=70, min_length=30,
#                                              max_length=50)
#         # scores_t = output_t[0][0].detach().numpy()
#         gen_text_body = tl_model.tokenizer_t.batch_decode(output_t, skip_special_tokens=True)
#
#         predict_t = dict()
#
#         self.response["title"] = gen_text_body[0]
#
#     def get_response(self):
#         return self.response
#
#
# if __name__ == '__main__':
#     text = "Horrible customer service. Receptionist is extremly rude. I have called regarding a roofing report weekly for over a month and never received the report. I asked to hold to speak with a manager or the owner and was told by the receptionsit that she didn't control."
#     obj_t = TitleGenerator(text)
#     obj_t.get_title()
#     obj_t.get_response()
