# Spam Email Detection App

A Flask web application that detects spam emails using machine learning.

## Important Features

- **Web Interface**: Input email text and get immediate spam/not spam classification
- **API Access**: REST endpoint for programmatic integration
- **Responsive Design**: Works on desktop and mobile devices
- **Machine Learning**: Uses Naive Bayes classifier for prediction

## Quick Setup

1. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```
   python app.py
   ```

3. **Access the app**:
   ```
   http://localhost:5000
   ```

## API Usage

Send POST requests to `/api/predict` with JSON:

```json
{
  "email": "Your email content here"
}
```

Response:
```json
{
  "email": "Your email content here",
  "prediction": "spam" or "ham"
}
```

## Project Structure

- `app.py` - Main Flask application
- `utils.py` - Model loading and prediction functions
- `models/` - Contains the trained model file
- `static/` - CSS and JavaScript files
- `templates/` - HTML templates

## Technical Info

- **Backend**: Flask
- **Frontend**: Bootstrap 5
- **ML Model**: Naive Bayes (`clf_NaiveBaised.pkl`)
- **Debug Mode**: Enabled for development

## Requirements

- Python 3.7+
- Flask
- NumPy
- scikit-learn (for the model)
