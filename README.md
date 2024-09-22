Heart Attack Prediction Model with FastAPI
This repository contains a machine learning model for heart attack prediction, deployed using FastAPI on an AWS EC2 instance. The application predicts the likelihood of a heart attack based on several medical and lifestyle features. The model is a DecisionTreeClassifier trained using the heart.csv dataset.

Features
FastAPI Framework: The backend API is built with FastAPI, which provides high performance and automatic documentation.
Machine Learning Model: A heart attack prediction model using DecisionTreeClassifier from scikit-learn.
REST API Endpoints:
GET /: Returns a welcome message to confirm the API is running.
POST /heart/predict: Predicts the likelihood of a heart attack based on user input.
Deployment: The application is deployed on an Ubuntu EC2 instance using uvicorn as the ASGI server and managed via systemd.
Technologies Used
Python 3.8+
FastAPI
Uvicorn
Scikit-learn
Joblib for model serialization
AWS EC2 for deployment
Git for version control
Machine Learning Model
The model was trained using a dataset (heart.csv) that contains the following features:

age: Age of the person
sex: Gender (0 = Female, 1 = Male)
cp: Chest pain type
trtbps: Resting blood pressure (in mm Hg)
chol: Cholesterol level (in mg/dl)
fbs: Fasting blood sugar (1 = True, 0 = False)
restecg: Resting electrocardiographic results
thalachh: Maximum heart rate achieved
exng: Exercise-induced angina (1 = Yes, 0 = No)
oldpeak: ST depression induced by exercise relative to rest
slp: Slope of the peak exercise ST segment
caa: Number of major vessels colored by fluoroscopy
thal: Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)
The target variable (output) represents whether the patient is likely to have a heart attack.


Usage
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/udayangani/Heart-attack-prediction-model.git
2. Install Dependencies
After cloning the repository, install the required dependencies listed in the requirements.txt file.

3. Train the Model
The model has already been trained and saved as heart.joblib. However, if you want to retrain the model, you can modify and run the training script provided in the repository.

4. Run the FastAPI Application
Once the setup is complete, you can run the FastAPI application using uvicorn or deploy it on a server using systemd (as described in the deployment section).

Deployment
The application has been deployed on an AWS EC2 instance using uvicorn as the ASGI server. For details on deployment, please refer to the "Deployment" section of the repository.

Contact
For any questions or issues, feel free to contact me:

Email: udayanganishiranthika@gmail.com
GitHub: udayanagani
