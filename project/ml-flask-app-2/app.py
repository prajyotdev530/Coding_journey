from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model (make sure model.pkl is in the same folder)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        rank = float(request.form['rank'])
        input_data = np.array([[rank]])
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Predicted Salary: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)