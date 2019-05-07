******************************************************
Direction For Developers: 
To install and run the API on your server please do the following: 
Using Following IP Address:
3.82.144.187:8080
You will need to pip install the following libraries: 
1. Numpy (including random)
2. Sys
3. Re
4. Glob
5. Nltk
6. TextBlob
7. Textblob.en.sentiments
8. Textblob.np.extractors
9. Textblob.classifiers
Code Explanation: 
1.  (Lines 18-29) - First we have to check that there are no special characters in the user input for the code to run – if there is a special character the text will not be accepted and the user will get an error
2. (Line 25)If the text does not have special characters – the user is prompted to choose how they want to analyze the text (e.g. Tags, Sentiment, Noun Phrases, Sentences or Translate)
3. (Lines 53-55) If the user selects Tags then return the tags to each word
4. (Lines 56-63) If Sentiment - we perform sentiment analysis to check if the text is positive or negative 
a. We then provide an output to the user telling if it is positive or negative 
5. (Lines 65-67) If Noun Phrases – we perform noun_phrases function and return the result
6. (Lines 68-70) if Ngrams – we perform ngrams function and return the result
7. (Lines 71-89) If Sentences – we direct the user to the following options
a. Which sentence would the like to view 
b. Would they like to count the # of words in the sentence
c. Would they like to display word inflection 
d. Enter any number index that they would like to singularize 
8. Each of these will give the user an output depending on their selection 
9. (Lines 91-128) If they choose the translate option – we have them select one of the following languages to translate 

a. English 
b. Arabic 
c. Chinese 
d. Spanish 
e. Thai
f. Russian
g. Portuguese
h. Japenese
i. Greek
j. German
k. French
l. Dutch
10.  Depending on the users selection we return the translated text 
**********************************************************************************
