# Importing necessary modules
import uvicorn
from fastapi import FastAPI
import joblib
from heartuser import heartuser

# Initialize the FastAPI app
app = FastAPI()

# Load the pre-trained machine learning model using joblib 
joblib_in = open("heart.joblib","rb")
model=joblib.load(joblib_in)

#Define the root route which will return a simple message when accessed
@app.get('/')
def index():
    return {'message': 'Heart attack prediction model'}

# Define a POST route to predict heart attack risk based on user input
@app.post('/heart/predict')
def heart_type(data:heartuser):
    data = data.dict()

    # Extracting individual feature values from the input data
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

    # Use the model to predict heart attack risk based on input data
    prediction = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thal]])
    
    # Return the prediction result
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
