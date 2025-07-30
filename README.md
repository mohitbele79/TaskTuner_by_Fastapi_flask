# TaskTuner – Workload Balancer

### Aim
TaskTuner is a smart workload management tool. It ingests tasks with estimated effort, schedules them under a daily limit, and displays the plan in a user-friendly calendar interface. Tasks can be sourced from Trello, Asana, or mock data.

---

##  Features
-  Fetch tasks from mock API or integrate with Asana (free tier).
-  Input effort estimates per task.
-  Greedy scheduling to balance tasks across days with an hour limit.
-  Web UI with calendar/table view (Flask frontend).
-  Backend API with FastAPI.
-  Unit testing for scheduling logic.
-  Documentation with API usage, setup guide, and screenshots.

---

##  Project Structure

TaskTuner/
├── backend/
│ ├── app.py # FastAPI backend server
│ ├── scheduler.py # Scheduling algorithm logic
│ └── tests/
│ └── test_scheduler.py # Unit tests for scheduler
├── frontend/
│ ├── app.py # Flask frontend app
│ └── templates/
│ └── index.html # HTML UI page
├── data/
│ ├── sample_tasks.json # Mock tasks data
│ └── efforts.json # User-submitted efforts (saved)
├── README.md # This file
|
└── screenshots # UI demo proof


## Setup

### 1. Clone the Repo
```bash
git clone https://github.com/mohitbele79/TaskTuner_by_Fastapi_flask.git
cd tasktuner

### 2. Backend Setup (FastAPI) 
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --port 8000

### 3. Frontend Setup (Flask) 

cd ../frontend
pip install -r requirements.txt
python app.py

### 4. Open the UI
Visit: http://127.0.0.1:5000


## API Endpoints
- `GET /tasks`
- `POST /tasks/effort`
- `GET /schedule?startDate=YYYY-MM-DD`

##Scheduling Logic (Greedy Heuristic)
- Tasks sorted by priority: High → Medium → Low.
- Scheduled to days with a max daily hour limit (default 8 hrs/day).
- Tasks with more effort are split across days if needed.
- Real logic in scheduler.py, mocked schedule used for early testing.

## Running Tests
cd backend
pytest




