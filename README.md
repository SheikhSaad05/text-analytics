![pythonbadge](https://img.shields.io/badge/Python-3-green)
![pythonbadge](https://img.shields.io/badge/Markovify-0.9.3-orange)
![pythonbadge](https://img.shields.io/badge/GPT2-Model-blue)
![pythonbadge](https://img.shields.io/badge/Transformer-API-success)
![pythonbadge](https://img.shields.io/badge/Huggingface-API-critical)
![pythonbadge](https://img.shields.io/badge/Trafilatura-0.9.1-blueviolet)
![pythonbadge](https://img.shields.io/badge/Pytorch-1.8.1-important)


# Sentiment and Emotion Analysis

An AI based text analytics which uses Natural Language Processing(NLP) and several other ML approches to analyse text sentiments by classifiying the positives text from negative text and emotions by classifying into happy, sad, anger, joy and more. 

## Approch

This is done by following a sequence of steps needed to solve. We will start with detecting the language of raw text of the blog then preprocessing and cleaning of raw text of the blogs. Then we wil explore the cleaned text and try to get some intution about the context of the tweets. After that numerical features from data will be extracted and using these features we identify the sentiments and emotions of text.

## A typical top-level directory structure

```
text-analytics

├── app
│   ├── strategy
│   	├── __init__.py            		# Main file for model calling and predictions
|	├── data_models.py
	├── keywords.py                        # Run
	├── prediction.py
	├── title.py
	├── utilities.py 
│   ├── __init.py
│      
├── test   
│   └── test.py				# Unit and Integration testing of the module 
├── run.py					# run      
└── requirements.txt				# Listing all the requirements for PIP Installation
```
## Technologies Used

- Python3
- Pytorch
- NLTK package
- Pyenchant package for English grammar rules
- Bert Extractive Summarizer
- GPT2 medium : For text-based on prompt generation
- Transformer : Transformer pipeline for GPT2 pre-trained model
- Markovify : Python3 package for prompt generation. It is replaced with BERT but Markovify is still being using for concluding sentence creation
- Textstat for reading level
- GingerIt :  For grammar and spelling correction ( Python3 package ). This is now replaced with Rule-based techniques mentioned in the source code and the attached detailed document. 
- Docker
- GPU


## API Usage

Here "text" can be equals to 'paragraph'
end point for API request with type: /predictions


### API Request With Type
```
{
    "query":"http://localhost:5000/predictions?text",
    "text":"This project is subset of Data Science project in ContentStudio.io"
}
```


## Setup Guide

1. Clone the repository
   ```
   git clone https://github.com/d4interactive/text-analytics
   ```
2. Change Directory
   ```
   cd text-analytics
   ```
3. Create a Virtual Environment 
   ```
    python3 -m venv venv
    source venv/bin/activate
   ```
4. Install requirements
    ```
   pip3 install -r requirements.txt
   ```
5. Download Spacy model 
   ```
   python -m spacy download en_core_web_sm 
   python -m spacy download en
   ```
6. Run command (The URL can be replaced with someother url)
    ```
    python3 run.py 
    ```
7. Run Unit Tests
   ```
   coverage run -m tests.test_text_sentiments
