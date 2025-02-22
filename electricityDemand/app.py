from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
from datetime import datetime
from test import heures_ecoulees
app = Flask(__name__)


initial = "2022-01-01 01:00:00"

# Charger les modèles
with open('models/Holt_Winters_additif.pkl', 'rb') as f:
    model1 = pickle.load(f)
with open('models/Holt_Winters_multiplicatif.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('models/arima.pkl', 'rb') as f:
    arima  = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['datetime']
    input_date = datetime.fromisoformat(user_input)#datetime.strptime(user_input, '%Y-%m-%d %H:%M')
    print(input_date)
    features = pd.DataFrame({
        'year': [input_date.year],
        'month': [input_date.month],
        'day': [input_date.day],
        'hour': [input_date.hour],
        'minute': [input_date.minute]
    })

    index1 = int(heures_ecoulees(initial, input_date.strftime('%Y-%m-%d %H:%M:%S'))) #model1.predict(features)[0]
    index2 = int(heures_ecoulees(initial, input_date.strftime('%Y-%m-%d %H:%M:%S'))) #model2.predict(features)[0]

    print(model1.predict(index1, index1))

    return jsonify({
        'model1_prediction': model1.predict(index1, index1).values.sum()*42472.83,#prediction1,
        'model2_prediction': model2.predict(index1, index1).values.sum()*42472.83,
        'arima' :arima.predict(index1, index1).values.sum()*42472.83
        })
    

if __name__ == '__main__':
    app.run(debug=True)
