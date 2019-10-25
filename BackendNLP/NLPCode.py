import nltk
import string
import re
import sklearn
from sklearn.feature_extraction.text import CountVectorizer 

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
    tag = nltk.pos_tag(processedQuery) 
    parsed = [word for word,pos in tag if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'JJ' or pos == 'VB')]
    processedQuery = str(parsed)
    return processedQuery

def bagOfWords(preProcessed):
    iterable = ['husband', 'tri', 'chemo', 'morn', 'platelet', 'count', 'low', 'needle', 'low', 'stay', 'posit', 'get', 'hard', 'stay', 'posit', 'cours', 'sad', 'front', 'el', 'ani', 'input', 'blood', 'level', 'allow', 'eat', 'much', 'potassium', 'appreci', 'input']
    count_vect = CountVectorizer()
    X_counts = count_vect.fit_transform(processedQuery)
    print(vectorizer.get_feature_names())


##read the input from the end user
##query = input("Enter the user query:")
query = "Husband tried to do chemo this morning but platelet counts were to low needless to say that brought his spirits down low too. I am trying to stay positive for him but it's getting so hard to stay positive. Of course I don't show my sadness in front of him but what else can be done? Any input of how we can get his blood levels back up? He's on bactrim so he's not allowed to eat anything with much potassium. Appreciate any input."

##preprocessing data - removing punctuations, stopwords, stemming and lemmatization 
processedQuery = removePunct(query)
processedQuery = tokenize(processedQuery)
processedQuery = removeStopword(processedQuery)
processedQuery = stemmer(processedQuery)
processedQuery = lemmatizing(processedQuery)
processedQuery = posTagging(processedQuery)
print(processedQuery)

##featue vector generation - using bag of words and print features 

##feature vector generation - using n-gram and print features 

##feature vector generation - using TF-IDF and print features 

##cosine similarity 