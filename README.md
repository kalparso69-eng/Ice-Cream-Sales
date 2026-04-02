# Ice Cream Sales Predictor

A web-based application that predicts ice cream sales based on temperature, rainfall, day of the week, and month using a machine learning model.

## Features

- Predict ice cream sales using historical data
- Web interface for easy input
- REST API endpoint for predictions

## Installation

1. Install Python 3.7+
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Train the model:

   ```
   python train_model.py
   ```

2. Run the Flask app:

   ```
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000`

4. Enter the parameters and click "Predict Sales"

## API Usage

Send a POST request to `/predict` with JSON data:

```json
{
  "temperature": 32,
  "rainfall": 0.5,
  "day_of_week": 5,
  "month": 4
}
```

Response:

```json
{
  "predicted_sales": 245
}
```

## Files

- `app.py`: Flask application
- `train_model.py`: Model training script
- `ice_cream_model.pkl`: Trained model
- `templates/index.html`: Web interface
- `static/style.css`: CSS styling
- `static/script.js`: JavaScript for form handling
- `requirements.txt`: Python dependencies
