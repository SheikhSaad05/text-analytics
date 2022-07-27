# import numpy as np
# from scipy.special import softmax
# from app.strategy.data_models import Entities
#
# entity_model = Entities()
#
#
# class EntityExtraction:
#
#     def __init__(self, text):
#         self.text = text
#         self.response = dict()
#
#     def convert(self):
#         lst = self.text.split(" ")
#         self.response['words'] = lst
#
#     def entity_extraction(self):
#         """
#
#         :return:
#         """
#         encoded_input_ent = entity_model.tokenizer_entities(self.text, return_tensors='pt')
#         output_ent = entity_model.Model_Entities(**encoded_input_ent)
#
#         labelids = output_ent.logits.squeeze().argmax(axis=-1)
#         ent_labels = [entity_model.Model_Entities.config.id2label[int(x)] for x in labelids]
#         ent_labels = ent_labels[1:-1]
#         self.response['entities'] = ent_labels
#
#     def get_response(self):
#         print(self.response)
#         return self.response
#
#
# if __name__ == '__main__':
#     text = "Flight 976 from John F. Kennedy International Airport in New York City to Santa Ana, California, landed in Denver safely where police removed and apprehended the passenger, the airline said. A source familiar with the details of the incident said the attack was unprovoked, adding the passenger went to the back of the plane and punched the flight attendant twice in the face and broke her nose."
#     obj = EntityExtraction(text)
#     obj.convert()
#     obj.entity_extraction()
#     obj.get_response()
