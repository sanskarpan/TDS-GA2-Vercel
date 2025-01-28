from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json, os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Corrected file path to point to the root directory
file_path = os.path.join(os.path.dirname(__file__), "../students.json")

# Load marks data
with open(file_path, "r") as f:
    students = json.load(f)

# Create a dictionary for fast lookup
marks_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    results = [marks_dict.get(student, None) for student in name]
    return JSONResponse(content={"marks": results})
