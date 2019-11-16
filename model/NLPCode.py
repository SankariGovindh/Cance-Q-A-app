from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import joblib
import nltk
import re 
import string 
import math 

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

TOP_K = 5

with open('vectors.pkl', 'rb') as f:
    tfidf_matrix, ids = pickle.load(f)
tfidf_vectorizer = joblib.load('vectorizer.joblib')

query = preProcess(test_query)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_vectorizer.transform([' '.join(query)])).reshape(-1)
cosine_similarities = cosine_similarities[cosine_similarities > 0.0]
if cosine_similarities.tolist():
    raise Exception('No similar questions found!!')
top_k_max_indices = cosine_similarities.argsort()[-TOP_K:][::-1]
top_k_question_ids = np.array(ids)[top_k_max_indices]