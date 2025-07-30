from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

@app.get("/tasks")
def get_tasks():
    try:
        with open(DATA_DIR / "sample_tasks.json") as f:
            tasks = json.load(f)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks/effort")
def set_effort(payload: dict):
    task_id = payload.get("taskId")
    hours = payload.get("hours")
    if not task_id or hours is None:
        raise HTTPException(status_code=400, detail="Missing taskId or hours")

    efforts_file = DATA_DIR / "efforts.json"
    try:
        if efforts_file.exists():
            with open(efforts_file) as f:
                efforts = json.load(f)
        else:
            efforts = {}

        efforts[task_id] = hours

        with open(efforts_file, "w") as f:
            json.dump(efforts, f)

        return {"message": "Effort saved."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/schedule")
def get_schedule(startDate: str):
    # Return a mock schedule
    schedule = [
        {
            "date": startDate,
            "task": {"id": "1", "name": "Write Docs", "priority": "High"},
            "effort": 2
        },
        {
            "date": startDate,
            "task": {"id": "2", "name": "Build API", "priority": "Medium"},
            "effort": 4
        }
    ]
    return schedule
