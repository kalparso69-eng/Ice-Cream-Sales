from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'ice_cream_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    temperature = data['temperature']
    rainfall = data['rainfall']
    day_of_week = data['day_of_week']  # 0-6, Monday=0
    month = data['month']  # 1-12

    # Prepare input
    input_data = pd.DataFrame([[temperature, rainfall, day_of_week, month]],
                              columns=['Temperature', 'Rainfall', 'DayOfWeek', 'Month'])

    prediction = model.predict(input_data)[0]
    return jsonify({'predicted_sales': round(prediction)})

if __name__ == '__main__':
    app.run(debug=True)