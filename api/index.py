# api/index.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Allows only GET requests
    allow_headers=["*"],  # Allows all headers
)

# Load student data
with open('data/students.json', 'r') as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "No names provided"}
    
    marks = []
    for student_name in name:
        mark = students_data.get(student_name, None)
        marks.append(mark)
    
    return {"marks": marks}

# Root endpoint for testing
@app.get("/")
async def root():
    return {"status": "API is running"}