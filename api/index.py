from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data
with open("data/students.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    results = [marks_data.get(student, None) for student in name]
    return JSONResponse(content={"marks": results})
