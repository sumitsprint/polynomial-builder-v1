from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
    print(coordinates)
    return {"message": "Analysis complete!"}
#     # Perform analysis on the coordinates
#     # For example, you could calculate the polynomial coefficients here
#     # and return them as a response
#     return {"hello This is the analysis result!"}




