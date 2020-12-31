# importing required libraries
import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from joblib import dump


data = pd.read_csv('dataset/twitter_sentiments.csv')
train, test = train_test_split(data, test_size = 0.2, stratify = data['label'], random_state=21)

tfidf_vectorizer = TfidfVectorizer(lowercase= True, max_features=1000, stop_words=ENGLISH_STOP_WORDS)
tfidf_vectorizer.fit(train.tweet)

train_idf = tfidf_vectorizer.transform(train.tweet)
test_idf  = tfidf_vectorizer.transform(test.tweet)

model_LR = LogisticRegression()
model_LR.fit(train_idf, train.label)

# predict_train = model_LR.predict(train_idf)
# predict_test = model_LR.predict(test_idf)


## f1 score on train data
# f1_score(y_true= train.label, y_pred= predict_train)
# f1_score(y_true= test.label, y_pred= predict_test)

pipeline = Pipeline(steps= [('tfidf', TfidfVectorizer(lowercase=True, max_features=1000, stop_words= ENGLISH_STOP_WORDS)), ('model', LogisticRegression())])

pipeline.fit(train.tweet, train.label)
#pipeline.predict(train.tweet)
#text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]
#pipeline.predict(text)

dump(pipeline, filename="text_classification.joblib")

##Get Model
#from joblib import load
#text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]
#pipeline = load("text_classification.joblib")
#pipeline.predict(text)