# utils.py (Helper Functions)
import pickle
import numpy as np

def load_model():
    """
    Loads the trained model from file.
    """
    with open("models/clf_NaiveBaised.pkl", "rb") as file:
        model = pickle.load(file)  # Load the model using pickle
    return model

def model_predict(features):
    """
    Predicts using the loaded model.
    """
    model = load_model()  # Hint: Load the model before predicting
    prediction =  model.predict([features]) # Hint: Use the correct method to make predictions
    # If the email is spam, prediction should be 1, otherwise -1
    prediction = 'ham' if prediction[0] == 0 else 'spam'
    return prediction