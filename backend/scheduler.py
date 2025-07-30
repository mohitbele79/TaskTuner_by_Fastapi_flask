def generate_schedule(tasks, efforts, start_date, daily_limit=6):
    from datetime import timedelta
    scheduled = {}
    current_date = start_date
    total_hours = 0
    daily_tasks = []

    for task in tasks:
        hours = efforts.get(task["id"], 1)
        if total_hours + hours > daily_limit:
            scheduled[str(current_date)] = daily_tasks
            current_date += timedelta(days=1)
            daily_tasks = []
            total_hours = 0
        daily_tasks.append(task)
        total_hours += hours

    scheduled[str(current_date)] = daily_tasks
    return scheduled

