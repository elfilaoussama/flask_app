import pickle
import numpy as np

def load_model():
    """
    Loads the trained model from file.
    """
    # load the vectorizer
    with open('models/clf_NaiveBaised.pkl', 'rb') as fd:
        model = pickle.load(fd)

    return model

def model_predict(features):
    """
    Predicts using the loaded model.
    """
    model = load_model() # Hint: Load the model before predicting
    prediction =  model.predict([features])# Hint: Use the correct method to make predictions
    # If the email is spam, prediction should be 1, otherwise -1
    prediction =  'ham' if prediction[0] == 0 else 'spam'
    return prediction
