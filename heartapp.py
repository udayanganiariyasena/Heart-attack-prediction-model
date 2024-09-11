import uvicorn
from fastapi import FastAPI
import joblib
from heartuser import heartuser

app = FastAPI()
joblib_in = open("heart.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Heart attack prediction model test'}

@app.post('/heart/predict')
def heart_type(data:heartuser):
    data = data.dict()
    age = data['age']
    sex = data['sex']
    cp = data['chest_pain_type']
    trtbps = data['resting_blood_pressure']
    chol = data['cholesterol_level']
    fbs = data['fasting_blood_sugar']
    restecg = data['resting_electrocardiographic_results']
    thalachh = data['maximum_heart_rate_achieved']
    exng = data['exercise_induced_angina']
    oldpeak = data['oldpeak']
    slp = data['slope_of_the_peak_exercise']
    caa = data['Number_of_major_vessels_colored_by_fluoroscopy']
    thal = data['thalassemia']
    prediction = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thal]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)