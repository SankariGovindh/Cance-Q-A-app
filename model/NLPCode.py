import mysql.connector 
import nltk
import string
import re
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import math 
import json 

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

content = []
tfidf = [] ##storing the vector of every question in a list

##connecting to a MySQL database 
db = mysql.connector.connect(host="inventory-1.cs45dfwrhl7w.us-west-1.rds.amazonaws.com",
                     user="administrator",
                     passwd="Cancerbase2019",
                     db="inventory")

cursor = db.cursor()

##querying all the questions from the table 
cursor.execute("SELECT content FROM question")

##reading data from database 
for record in cursor:
    query = ''.join(record)
    content.append(preProcess(query))

##passing the content list to TFIDF Vector to create vectors 
def tfidfVectorizer(content): 
    tfidf_vectorizer = TfidfVectorizer()
    for i in content:
        tfidf_matrix = tfidf_vectorizer.fit_transform(i)
        print(tfidf_matrix.toarray())

def termFrequency(term, content):
    normalizeDocument = content #current question that is passed 
    return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))


def inverseDocumentFrequency(term, content):
    numDocumentsWithThisTerm = 0
    for doc in content:
        if term.lower() in doc:
            numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1
 
    if numDocumentsWithThisTerm > 0:
        return 1.0 + math.log(float(len(content)) / numDocumentsWithThisTerm)
    else:
        return 1.0

cursor.close()

i = 1 
data = {}

for string in content:
    c = ' '.join(string)
    terms = c.split()
    for term in terms: 
        tf = termFrequency(term,string)
        idf = inverseDocumentFrequency(term,content)
        tfidf.append(tf*idf)
    ##end of inner for     
    
    ##dumping to a JSON file 
    data[i] = []
    data[i].append(tfidf)
    with open('data.txt', 'w') as outfile:
        json.dump(data,outfile)
    tfidf = [] ##clearing the list to store the new values 
    i += 1 

##performing cosine similarity between the user input query and returning the question index 
