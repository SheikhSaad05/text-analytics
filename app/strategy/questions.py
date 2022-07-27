# import json
#
# from app.strategy.data_models import Questions
import requests


# qw_model = Questions()


class QuestionExtraction:

    def __init__(self, text):
        self.text = text
        self.response = dict()

    def question_extraction(self):
        # input_ids = qw_model.tokenizer_questions.encode(self.text, return_tensors="pt")
        # res = qw_model.Model_questions.generate(input_ids,do_sample=True, **generator_args, num_return_sequences=3)
        # output = qw_model.tokenizer_questions.batch_decode(res, skip_special_tokens=True)

        try:
            output = requests.get('http://localhost:5012/questions?text={}'.format(self.text))
        except:
            output = requests.get('http://question:5012/questions?text={}'.format(self.text))

        output = output.json()
        output = output.get('questions')

        # print(output)
        self.response['questions'] = output

    def get_response(self):
        print(self.response)
        return self.response


if __name__ == '__main__':
    text = "In tech news, Facebook was busily exploiting the tone deaf policy of getting slightly irritated with growing pressure from whistleblowers, former venture capital critics who built their careers on the company’s early success, and a two-fisted teamup from a Congress in over its head and the media looking for a good story to replace Donald Trump’s devolution as credible threat. Today, Facebook ads talk of reforming Section 230 and otherwise providing rules for the company to follow. Infrastructure bingo has whittled down the cost by 60%; the plan is to get it passed in time to influence the election of the Governor of Virginia."
    obj = QuestionExtraction(text)
    obj.question_extraction()
    obj.get_response()


