import json
import requests

url = "http://127.0.0.1:8000/diabetics_prediction"
input_data = {
    'Pregnancies': 1,
    'Glucose': 126,
    'BloodPressure': 60,
    'SkinThickness': 0,
    'Insulin': 0,
    'BMI': 30.1,
    'DiabetesPedigreeFunction': 0.349,
    'Age': 45

}
response = requests.post(url, json=input_data)
print(response.text)