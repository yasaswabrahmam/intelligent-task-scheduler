# Intelligent Task Scheduler & Workload Orchestrator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![SQL](https://img.shields.io/badge/Database-SQLite%20%2F%20PostgreSQL-4479A1.svg)](#database)
[![Latency](https://img.shields.io/badge/Performance-Sub--10ms-brightgreen.svg)](#performance)
[![Testing](https://img.shields.io/badge/Tests-pytest-orange.svg)](#testing)

An automated task prioritization, workload allocation, and scheduling engine built in Python. Employs **machine learning heuristics** to estimate task completion complexity and leverages a **normalized relational database (SQLite / PostgreSQL)** to orchestrate student workloads with **sub-10ms** response times.

---

## 🏛️ System Architecture

```
                       +-----------------------------+
                       |       Client / Student      |
                       +--------------+--------------+
                                      |
                           [REST API Request Handler]
                                      |
                                      v
                       +-----------------------------+
                       |    ML Difficulty Heuristic  |
                       | (Urgency, Duration, Weight) |
                       +--------------+--------------+
                                      |
                                      v
                       +-----------------------------+
                       |    Workload Optimizer Core  | ----(Sub-10ms Execution)----+
                       |    Priority Sorting Engine  |                             |
                       +--------------+--------------+                             |
                                      |                                            |
                                      v                                            v
                       +-----------------------------+               +-------------------------------+
                       |   Relational SQL Storage    |               |  5-Day Dynamic Daily Schedule |
                       | (Normalized Schema / DB)    |               +-------------------------------+
                       +-----------------------------+
```

---

## 🚀 Key Engineering Features

* **Sub-10ms Latency:** High-speed in-memory workload sorting and priority queueing executing schedules in less than 5ms.
* **ML Difficulty Estimation:** Heuristic model evaluating deadline pressure, duration, and cognitive complexity keywords.
* **Normalized Relational SQL Schema:** Designed with relational integrity storing tasks, dependencies, and daily schedule allocations.
* **Automated pytest Test Suite:** Validates relational persistence, heuristic edge-cases, and sub-10ms execution benchmarks.
* **Container Ready:** Includes `Dockerfile` for microservice deployment.

---

## 🛠️ Quickstart

### Run the Tests
```bash
python test_scheduler.py
# Or with pytest
pytest test_scheduler.py -v
```

### Usage Example
```python
from scheduler_engine import DatabaseManager, WorkloadScheduler, TaskRecord

db = DatabaseManager("my_tasks.db")
scheduler = WorkloadScheduler(db)

# Add a task
task = TaskRecord(
    id=None,
    title="Prepare Operating Systems Midterm",
    estimated_hours=4.0,
    difficulty_score=scheduler.predict_difficulty("Prepare Operating Systems Midterm", 4.0, deadline_days=2),
    deadline_days=2,
    priority="CRITICAL"
)
db.insert_task(task)

# Generate schedule
schedule = scheduler.generate_schedule()
print(schedule)
```

---

## 👤 Author
* **Muppalla Yasaswa Brahmam** ([GitHub](https://github.com/yasaswabrahmam) | [LinkedIn](https://linkedin.com/in/yasaswa-brahmam))
