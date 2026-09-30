"""
Unit & Performance Tests for Intelligent Task Scheduler
Executed with pytest
"""
import unittest
from scheduler_engine import DatabaseManager, WorkloadScheduler, TaskRecord

class TestWorkloadScheduler(unittest.TestCase):
    def setUp(self):
        # In-memory database for fast, isolated testing
        self.db = DatabaseManager(":memory:")
        self.scheduler = WorkloadScheduler(self.db)

    def test_database_persistence(self):
        task = TaskRecord(
            id=None,
            title="Prepare Operating Systems Lab",
            estimated_hours=3.5,
            difficulty_score=0.75,
            deadline_days=2,
            priority="HIGH"
        )
        task_id = self.db.insert_task(task)
        self.assertGreater(task_id, 0)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Prepare Operating Systems Lab")

    def test_difficulty_prediction_heuristic(self):
        score_high = self.scheduler.predict_difficulty("Distributed System Architecture Exam", hours=8.0, deadline_days=1)
        score_low = self.scheduler.predict_difficulty("Read Chapter 1 Intro", hours=1.0, deadline_days=10)
        self.assertGreater(score_high, score_low)

    def test_sub_10ms_latency(self):
        # Insert 20 tasks
        for i in range(20):
            self.db.insert_task(TaskRecord(
                id=None,
                title=f"Task {i}",
                estimated_hours=float(i % 5 + 1),
                difficulty_score=0.5,
                deadline_days=(i % 4 + 1),
                priority="NORMAL"
            ))

        result = self.scheduler.generate_schedule()
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["total_tasks_scheduled"], 20)
        self.assertLess(result["latency_ms"], 10.0, f"Latency {result['latency_ms']}ms exceeded 10ms target")

if __name__ == "__main__":
    unittest.main()
