# Import necessary libraries
from flask import Flask, request, render_template
import numpy as np
import pickle
import os 
# Initialize the Flask application
app = Flask(__name__)

# Load the trained machine learning model
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ensure 'gwp.pkl' is in the same directory as this script (the 'Flask' folder)
model_path = os.path.join(script_dir, 'gwp.pkl')

# Load the trained machine learning model using the full path
try:
    model = pickle.load(open(model_path, 'rb'))
    print("Model loaded successfully!")
except Exception as e:
    print(f"An error occurred while loading the model from {model_path}: {e}")
    model = None

# --- Define Routes for Web Pages ---

# Route for the Home Page
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')

# Route for the About Page
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

# Route for the Prediction Page
# This function handles both displaying the form and processing the submitted data
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Handles prediction requests.
    GET: Displays the prediction form.
    POST: Processes form data and returns the prediction.
    """
    if request.method == 'POST':
        if model is None:
            return "Model is not loaded. Cannot make a prediction.", 500
            
        # ... (inside the predict function)
        try:
            # 1. Retrieve all form values and convert to a list
            features = [
                int(request.form['quarter']),
                int(request.form['department']),
                int(request.form['day']),
                int(request.form['team']),
                float(request.form['targeted_productivity']),
                float(request.form['smv']),
                int(request.form['over_time']),
                int(request.form['incentive']),
                float(request.form['idle_time']),
                int(request.form['idle_men']),
                int(request.form['no_of_style_change']),
                float(request.form['no_of_workers']),
                int(request.form['month'])
            ]

            # 2. Convert to NumPy array for prediction
            final_features = np.array(features).reshape(1, -1)

            # 3. Use the model to get the numerical prediction
            prediction_value = model.predict(final_features)[0]

            # 4. Add the classification logic to determine the output text
            if prediction_value < 0.3:
                text = 'The employee is averagely productive.'
            elif prediction_value >= 0.3 and prediction_value <= 0.8:
                text = 'The employee is medium productive.'
            else:
                text = 'The employee is Highly productive.'

            # 5. Render the result page, passing the final descriptive text
            return render_template('result.html', prediction_text=text)

        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            return f"An error occurred: {e}", 400
    # If the request method is GET, just display the prediction form
    return render_template('predict.html')


# --- Main execution block ---
# This ensures the server runs only when the script is executed directly
if __name__ == "__main__":
    # Setting debug=True allows you to see errors and automatically reloads the server on code changes
    app.run(debug=True)
