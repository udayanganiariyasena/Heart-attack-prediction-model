import uvicorn
from fastapi import FastAPI
import joblib
from CarUser import CarUser

app = FastAPI()
joblib_in = open("car-recommender.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Cars Recommender ML API'}

@app.post('/car/predict')
def predict_car_type(data:CarUser):
    data = data.dict()
    age=data['age']
    gender=data['gender']

    prediction = model.predict([[age, gender]])

    print('')

    return {
        'prediction': prediction[0]
    }


@app.post('/car/predict/test')
def predict_car_type_test(data:CarUser):
    data = data.dict()
    age=data['age']
    gender=data['gender']

    prediction = model.predict([[age, gender]])

    print('')
    print('')
    print('')

    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)