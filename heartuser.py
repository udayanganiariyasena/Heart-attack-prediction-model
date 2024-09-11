from pydantic import BaseModel

# Define a Pydantic model to validate the input data for the heart attack prediction
class heartuser(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_blood_pressure: int
    cholesterol_level: int
    fasting_blood_sugar: int
    resting_electrocardiographic_results: int
    maximum_heart_rate_achieved: int
    exercise_induced_angina: int
    oldpeak: float
    slope_of_the_peak_exercise: int
    Number_of_major_vessels_colored_by_fluoroscopy: int
    thalassemia: int