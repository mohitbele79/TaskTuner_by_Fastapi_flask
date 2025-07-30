from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Point to FastAPI backend
BACKEND_URL = "http://127.0.0.1:8000"

@app.route("/")
def index():
    try:
        tasks = requests.get(f"{BACKEND_URL}/tasks").json()
        today = datetime.today().strftime('%Y-%m-%d')
        raw_schedule = requests.get(f"{BACKEND_URL}/schedule", params={"startDate": today}).json()

        # Build schedule dictionary
        schedule = {}
        for entry in raw_schedule:
            date = entry["date"]
            task = entry["task"]
            task["effort"] = entry["effort"]
            schedule.setdefault(date, []).append(task)

        # Load efforts from efforts.json (optional)
        try:
            with open("../data/efforts.json") as f:
                efforts = json.load(f)
        except FileNotFoundError:
            efforts = {}

    except Exception as e:
        flash(f"Error: {e}", "error")
        tasks, efforts, schedule = [], {}, {}

    return render_template("index.html", tasks=tasks, efforts=efforts, schedule=schedule)

@app.route("/update", methods=["POST"])
def update_effort():
    task_id = request.form.get("task_id")
    hours = request.form.get("hours")
    if not task_id or not hours:
        flash("Both Task ID and Hours are required.", "error")
        return redirect(url_for("index"))

    try:
        response = requests.post(f"{BACKEND_URL}/tasks/effort", json={"taskId": task_id, "hours": int(hours)})
        if response.status_code == 200:
            flash("Effort updated successfully!", "success")
        else:
            flash("Failed to update effort.", "error")
    except Exception as e:
        flash(f"Error: {e}", "error")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
