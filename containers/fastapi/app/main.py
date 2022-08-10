from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import pandas as pd
import pickle


with open("/opt/static/estimated.sav", "rb") as f:
    model = pickle.load(f)

class Input(BaseModel):
    age_group: str
    reported_race_ethnicity: str
    previous_births: str
    tobacco_use_during_pregnancy: str
    adequate_prenatal_care: str

app = FastAPI()
 
# for root endpoint
@app.get('/')
def main():
    return 'This endpoint accepts JSON encoded data in the /predict endpoint'

# /predict endpoint
@app.post("/predict")
async def predict(data: Input):
    response = jsonable_encoder(data)
    for key, value in response.items():
        response[key] = [value]
    prediction = model.predict(pd.DataFrame(response,index=[0]))
    if prediction[0] == 0:
        return "Full-term"
    else:
        return "Pre-term"

