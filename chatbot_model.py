import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_intent(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]