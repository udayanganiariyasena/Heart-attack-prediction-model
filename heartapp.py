import uvicorn
from fastapi import FastAPI
import joblib
from heartuser import heartuser

app = FastAPI()
joblib_in = open("heart.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Heart attack prediction model'}

@app.post('/heart/predict')
def heart_type(data:heartuser):
    data = data.dict()
    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trtbps = data['trtbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalachh = data['thalachh']
    exng = data['exng']
    oldpeak = data['oldpeak']
    slp = data['slp']
    caa = data['caa']
    thal = data['thal']
    prediction = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thal]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)