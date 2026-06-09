from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_input import validate_spacing
from degree_detection import detect_degree
import numpy as np


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from the backend!"}

@app.post("/analyse")
async def analyse(coordinates: List[dict]):
    x = [float(point['x']) for point in coordinates]
    y = [float(point['y']) for point in coordinates]
    x, y = validate_spacing(x, y)
    degree = detect_degree(y)
    coeffs = np.polyfit(x, y, degree)
    coeffs = np.round(coeffs, 10)
    coeffs[np.isclose(coeffs, 0)] = 0
    return {"degree": degree, "x": x.tolist(), "y": y.tolist(), "coeffs": coeffs.tolist()}



    
    






    




