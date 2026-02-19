import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int


    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'diabetic_model.sav')
scaler_path = os.path.join(base_path, 'scaler.sav')  # Path for your scaler

# Load BOTH the model and the scaler
diabetes_model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))
@app.post('/diabetics_prediction')
def diabeticsd_pred(input_parameters: model_input):
    input_list = [
        input_parameters.Pregnancies, input_parameters.Glucose,
        input_parameters.BloodPressure, input_parameters.SkinThickness,
        input_parameters.Insulin, input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction, input_parameters.Age
    ]
    input_scaled = scaler.transform([input_list])


    prediction = diabetes_model.predict(input_scaled)

    if (prediction[0] == 0):
        return "The person is non-diabetic"
    else:
        return "The person is diabetic"