from fastapi import FastAPI
from enum import Enum 

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

app = FastAPI()

@app.get('/ModelName/{model_name}')
async def get_model_name(model_name:ModelName):
    if (model_name == ModelName.alexnet):
        return {"model: ": model_name, "message": "alexnet training....."}
        
    if (model_name == ModelName.resnet):
        return {"model: ": model_name, "message": "resnet training....."}
    return {"model: ": model_name, "message": "lenet training....."}

