import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__,template_folder='templates')

model=pickle.load(open(r'C:\Users\rd\Desktop\Trisha files\project\model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    features=[np.array(int_features)]
    prediction=model.predict(features)
    if prediction[0]==1:
        output='Churn'
    elif prediction[0]==0:
        output='Not Churn'
    
    return render_template('index.html',prediction_text=f'The customer will {output}.')

if __name__=="__main__":
    app.run(debug=True)