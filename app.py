from flask import Flask,request,render_template

import pickle
import pandas as pd

model = pickle.load(open('model.pk','rb'))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('prediction.html')

@app.route('/predict',methods=['GET','POST'])

def predict():
    if request.method=='POST':
        Gender =int(request.form['gender'])
        Age = float(request.form['age'])
        Education=float(request.form['education'])
        Currentsmoker=int(request.form['currentsmoker'])
        cigperday=float(request.form['cigperday'])
        BPmed=int(request.form['BPmed'])
        PrprevalentStroke=int(request.form['prevalentstroke'])
        PrevalentHypertension=int(request.form['PrevalentHypertension'])
        Diabeties=int(request.form['diabeties'])
        SysBP=float(request.form['SysBP'])
        DiaBP=float(request.form['DiaBP'])
        BMI=float(request.form['BMI'])
        HeartRate=float(request.form['heartRate'])
        Glucose=float(request.form['glucose'])
        

        output = model.predict([[genter,age,education,currentsmoker,cigperday,BPmed,prevalentstroke,PrevalentHypertension,diabeties,SysBP,DiaBP,BMI,heartRate,glucose]])

        output = round(output[0],2)
        return render_template('prediction.html',predictions=output)


if __name__ == '__main__':
	app.run(debug=True)
