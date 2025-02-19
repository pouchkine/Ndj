from flask import Flask, render_template, request
#import pandas as pd
import pickle
from datetime import datetime

app = Flask(__name__)

# Charger le modèle ARIMA
with open('arma.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Récupérer la date entrée par l'utilisateur
        date_str = request.form['date']
        #date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Convertir la date en format utilisable par le modèle
        # (cela dépend de la façon dont votre modèle est entraîné)
        # Exemple : convertir en timestamp ou en jour de l'année, etc.
        # Ici, nous supposons que le modèle attend un timestamp
        #timestamp = date.timestamp()
        
        # Faire la prédiction
        prediction = model.predict(start=int(date_str), end=int(date_str))
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
