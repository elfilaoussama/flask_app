# Import necessary libraries
from flask import Flask, render_template, request, jsonify  # Import render_template for templates, request for form handling, and jsonify for JSON responses
from utils import model_predict

# Initialize Flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")  # Load the correct template file for the home page


@app.route('/predict', methods=['POST'])  # POST method should be used for form submission
def predict():
    """
    Handles form submission and returns prediction.
    """
    email = request.form.get('email')  # Get the email from the form using the 'email' field

    if not email:
        return render_template("index.html",
                               error="Email is required.")  # Send an error message if no email is provided

    prediction = model_predict([email])  # Use the model_predict function to get the prediction
    return render_template("index.html", email=email,
                           prediction=prediction)  # Return the email and prediction to the template


# Create an API endpoint
@app.route('/api/predict', methods=['POST'])  # POST method should be used for API predictions
def predict_api():
    """
    API endpoint that accepts a JSON payload and returns a prediction.
    """
    try:
        data = request.get_json()  # Extract JSON from the incoming request
        email = data.get('email')  # Safely get the email from the JSON payload

        if not email:
            return jsonify({'error': 'Email is required.'}), 400  # Return a 400 error if email is not provided

        prediction = model_predict([email])  # Get the prediction from the model
        return jsonify({'email': email, 'prediction': prediction})  # Return the email and prediction in a JSON response

    except Exception as e:  # Catch any potential exceptions
        return jsonify({'error': str(e)}), 400  # Return a 400 error with the exception message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run the app on host '0.0.0.0' and port '5000'
