from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('best_model_lgbm.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        PM10 = float(request.form['PM10'])
        CO = float(request.form['CO'])
        DEWP = float(request.form['DEWP'])
        SO2 = float(request.form['SO2'])
        TEMP = float(request.form['TEMP'])
        NO2 = float(request.form['NO2'])
        PRES = float(request.form['PRES'])
        O3 = float(request.form['O3'])
        WSPM = float(request.form['WSPM'])

        prediction=model.predict([[PM10,CO,DEWP,SO2,TEMP,NO2,PRES,O3,WSPM]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Try to input differet values.")
        else:
            return render_template('index.html',prediction_text="The prediction is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

