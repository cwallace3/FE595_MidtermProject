# Esther, Claude, Kenneth and Reinout

import re
import numpy as np
import glob
import nltk

# nltk.download()
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from textblob import TextBlob, Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.np_extractors import ConllExtractor
from textblob.classifiers import NaiveBayesClassifier
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random
from flask import Flask, render_template, request
import json

textcharacters = re.compile('[@_!#$%^&*()<>?/\|}{~;+]')
app = Flask(__name__)
firstclicktext = ''


# Function checks if the string
# contains any special character
def run(string):
    # Make own character set and pass
    # this as argument in compile method
    # Pass the string in search
    if (textcharacters.search(string) == None):
        textstring = "Your input has been accepted. \n"
        textstring = textstring + 'The following options are available to process input text: Tags, Sentiment, Noun Phrases, Ngrams, Sentences and Translate'
        return textstring
    else:
        return ("Your input has not been accepted.")


@app.route('/firstclick', methods=['POST'])
def firstclick():
    jsdata = request.form['x']
    print(jsdata)
    string = run(jsdata)
    return string


@app.route('/secondclick', methods=['POST'])
def secondclick():
    string = request.form['x']
    option = request.form['y']
    resp = start(string, option)
    return resp


def start(string, userchoiceless7):
    bbb = len(string.split())

    blob = TextBlob(string, analyzer=NaiveBayesAnalyzer())
    x = blob.sentiment

    if bbb < 100:

        # print("Polarity is: " + str(x))

        if (userchoiceless7.lower() == 'tags'):
            resp = str(blob.tags) + '\n'
            resp = resp + "Thank You!"
            resp = {'type': 'answer', 'answer': resp}

            return json.dumps(resp)
        elif (userchoiceless7.lower() == 'sentiment'):
            if x[0] == 'pos':
                resp = 'The sentiment of the input text is Positive' + '\n'
                resp = resp + "Thank You!"
                resp = {'type': 'answer', 'answer': resp}

                return json.dumps(resp)
            else:
                resp = 'The sentiment of the input text is Negative' + '\n'
                resp = resp + "Thank You!"
                resp = {'type': 'answer', 'answer': resp}

                return json.dumps(resp)

        elif (userchoiceless7.lower() == 'noun phrases'):
            resp = str(blob.noun_phrases) + '\n'
            resp = resp + "Thank You!"
            resp = {'type': 'answer', 'answer': resp}

            return json.dumps(resp)
        elif (userchoiceless7.lower() == 'ngrams'):
            resp = str(blob.ngrams(2)) + '\n'
            resp = resp + "Thank You!"
            resp = {'type': 'answer', 'answer': resp}

            return json.dumps(resp)
        elif (userchoiceless7.lower() == 'sentences'):
            jstext = {'type': 'input', "questions": ['Which sentence would you like to view? Enter index number here: ',
                                                     'Would you like to count the number of words in the sentence?',
                                                     'Would you like to display Word Inflection?',
                                                     'Enter any number index for the word you would like to singularize:']}
            return json.dumps(jstext)

        elif (userchoiceless7.lower() == 'translate'):
            jstext = {'type': 'input', "questions": ['Choose 1 translation option from the following list of languages: English, Arabic, Chinese, Spanish, Thai, Russian, Portuguese, Japenese, Greek, German, French, Dutch ']}
            return json.dumps(jstext)


    else:
        nouns = list()
        resp = ''

        for word, tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())

                resp = resp + "This text is about..."

                for item in random.choice(nouns, 5):
                    word = Word(item)
                    resp = resp + word.pluralize()
        resp = {'type': 'answer', 'answer': resp}

        return json.dumps(resp)


@app.route('/thirdclick', methods=['POST'])
def thirdclick():
    blob = request.form['x']
    type = request.form['y']
    jstext = request.form['js']

    if str(type).lower() == 'sentences':
        print(jstext)
        jsjson = json.loads(jstext)
        resp = sentances(jsjson['blob'], jsjson['answers'])
        return resp
    elif str(type).lower() == 'translate':
        print('translating')
        jsjson = json.loads(jstext)
        print(jsjson)
        resp = translate(jsjson['blob'], jsjson['answers'])
        return resp


def sentances(string, answers):
    bbb = len(string.split())

    blob = TextBlob(string, analyzer=NaiveBayesAnalyzer())
    x = blob.sentiment
    indexnumber = int(answers[0])
    wordcountinput = answers[1]
    inflectioninput = answers[2]
    inflectioninput2 = int(answers[3])

    resp = 'Total number of words in text entered is : ' + str(len(blob.words)) + '\n'
    resp = resp + 'Total number of sentences in text entered is : ' + str(len(blob.sentences)) + '\n'

    resp = resp + 'The text below corresponds to sentence # ' + str(indexnumber) + ':' + '\n'
    if (indexnumber > 0):
        resp = resp + str(blob.sentences[indexnumber - 1]) + '\n'
    else:
        resp = resp + str(blob.sentences[0]) + '\n'

    if (wordcountinput.lower()) == 'yes':
        resp = resp + 'The number of words in this sentence is: ' + str(len(blob.sentences[indexnumber - 1].words)) + '\n'
        if inflectioninput.lower() == 'yes':
            resp = resp + str(blob.sentences[indexnumber - 1].words[inflectioninput2].singularize()) + '\n'
            resp = resp + "Thank you!"

    return resp

def translate(string, answer):
    bbb = len(string.split())

    blob = TextBlob(string, analyzer=NaiveBayesAnalyzer())

    translate_response = answer[0]
    print(blob, translate_response)

    if (translate_response.lower() == 'english'):
        resp = str(blob.translate(to='en')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'arabic'):
        resp = str(blob.translate(to='ar')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'chinese'):
        resp = str(blob.translate(to='zh')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'spanish'):
        resp = str(blob.translate(to='es')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'thai'):
        resp = str(blob.translate(to='th')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'russian'):
        resp = str(blob.translate(to='ru')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'portuguese'):
        resp = str(blob.translate(to='pt')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'japenese'):
        resp = str(blob.translate(to='ja')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'greek'):
        resp = str(blob.translate(to='el')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'german'):
        resp = str(blob.translate(to='de')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'french'):
        resp = str(blob.translate(to='fr')) + '\n'
        resp = resp + "Thank you!"
        return resp
    elif (translate_response.lower() == 'dutch'):
        resp = str(blob.translate(to='nl')) + '\n'
        resp = resp + "Thank you!"
        return resp


@app.route('/')
def teststart():
    return render_template('start_page.html')


# Driver Code
if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=8080, debug= "TRUE")