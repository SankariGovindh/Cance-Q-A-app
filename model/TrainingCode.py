import mysql.connector 
import numpy as np 
import nltk, scipy
import string
import re
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import math 
import json, pickle
import joblib

def preProcess(query):             
             
    ##removing punctation 
    def removePunct(non_punctuation):
        non_punctuation = "".join([char for char in query if char not in string.punctuation]) ##if character not part of the string.punctuation list store as prossedData 
        return non_punctuation  

    ##tokenizing as separate words  
    def tokenize(tokens):
        tokens = re.split('\W+',processedQuery) ##tokenizing every word and separating the same using commas 
        return tokens 

    ##removing stopwords 
    def removeStopword(cleanData):
        stopwords = nltk.corpus.stopwords.words('english') ##storing all the stopwords for the English language 
        cleanData = [word for word in cleanData if word not in stopwords]
        return cleanData 

    ##stemming 
    def stemmer(currentData):
        stemming = nltk.PorterStemmer()
        stemmedData = [stemming.stem(word) for word in currentData]
        return stemmedData

    ##lemmatizing 
    def lemmatizing(currentData):
        lemma = nltk.WordNetLemmatizer()
        lemData = [lemma.lemmatize(word) for word in currentData]
        return lemData 

    ##part-of-speeching 
    def posTagging(processedQuery):
        tag = nltk.pos_tag([i for i in processedQuery if i]) 
        parsed = [word for word,pos in tag if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'JJ' or pos == 'VB')]
        return parsed

    processedQuery = removePunct(query)
    processedQuery = tokenize(processedQuery)
    processedQuery = removeStopword(processedQuery)
    processedQuery = stemmer(processedQuery)
    processedQuery = lemmatizing(processedQuery)
    processedQuery = posTagging(processedQuery)
    return processedQuery

##end of preProcess function

content, ids = [], []

##connecting to a MySQL database 
db = mysql.connector.connect(host="inventory-1.cs45dfwrhl7w.us-west-1.rds.amazonaws.com",
                     user="administrator",
                     passwd="Cancerbase2019",
                     db="inventory")

cursor = db.cursor()

##performing cosine similarity between the user input query and returning the question index 
test_query = "Does anyone know anything that will help with appetite?"


##querying all the questions from the table 
cursor.execute("SELECT content, question_id FROM question")


##reading data from database 
for question, question_id in cursor:
    query = question
    content.append(preProcess(query))
    ids.append(question_id)
    

##passing the content list to TFIDF Vector to create vectors 
def tfidfVectorizer(content, ids): 

    content = [' '.join(q) for q in content]

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(content)

    joblib.dump(tfidf_vectorizer, 'vectorizer.joblib')
    with open('vectors.pkl', 'wb') as f:
        pickle.dump([tfidf_matrix, ids], f)
        
##calling the tfidfcalc function to calculate the TFIDF vector values for the questions in the database 
tfidfVectorizer(content, ids)

