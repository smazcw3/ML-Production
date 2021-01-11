from flask import Flask, request
import joblib
#from joblib import dump, load
#import pickle

application = Flask(__name__)

vectorizer = joblib.load("vectorizer.pkl")
spam_ham_model = joblib.load("spam_ham_model.pkl")

# vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
# spam_ham_model = pickle.load(open('spam_ham_model.pkl', 'rb'))

@application.route('/')
def hello_world():
    return "Hello World"

@application.route('/spamorham', methods=['GET', 'POST'])
def spamorham():
    message = request.args.get("message")
    vect_message = vectorizer.transform([message])
    result = spam_ham_model.predict(vect_message)[0]
    return result 
#    return message

if __name__ == '__main__':
    application.run()
