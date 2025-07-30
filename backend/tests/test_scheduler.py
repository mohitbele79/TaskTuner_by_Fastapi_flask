import unittest
from datetime import date
from scheduler import generate_schedule

class TestScheduler(unittest.TestCase):
    def test_schedule(self):
        tasks = [{"id": "1", "name": "Task 1"}, {"id": "2", "name": "Task 2"}]
        efforts = {"1": 3, "2": 4}
        schedule = generate_schedule(tasks, efforts, date(2025, 1, 1), daily_limit=6)
        self.assertIn("2025-01-01", schedule)
        self.assertIn("2025-01-02", schedule)

if __name__ == '__main__':
    unittest.main()