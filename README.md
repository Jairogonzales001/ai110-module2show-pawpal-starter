# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

Today's Schedule
----------------
07:30 - Luna: Feed Luna (daily)
08:00 - Max: Morning walk (daily)
08:00 - Luna: Clean litter box (daily)
14:00 - Max: Vet appointment (one-time)

Conflict Warnings
-----------------
Conflict: Luna's task 'Clean litter box' is at the same time as Max's task 'Morning walk' at 08:00.

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```Run the test suite with:

```bash
python3 -m pytest
```

The tests verify:

- Marking a task as complete
- Adding tasks to a pet
- Sorting tasks by time
- Creating recurring daily tasks
- Detecting scheduling conflicts
```

Sample test output:

```
text
================================= test session starts ==================================
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/jairogonzales/ai110-module2show-pawpal-starter
collected 5 items

tests/test_pawpal.py .....                                                       [100%]

================================== 5 passed in 0.01s ===================================
```

**Confidence Level:** ⭐⭐⭐⭐☆

I am confident that the scheduler works correctly because all of the automated tests passed successfully. If I had more time, I would add more tests for edge cases like overlapping task durations and invalid time formats.   
```


## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all tasks from earliest to latest |
| Filtering | `filter_by_pet()`, `filter_by_status()` | Filters tasks by pet name or completion status |
| Conflict handling | `detect_conflicts()` | Warns when two tasks are scheduled for the same time |
| Recurring tasks | `mark_task_complete()`, `create_next_occurrence()` | Automatically creates the next daily or weekly task after completion |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Start the application and create an owner.
2. Add one or more pets to the owner.
3. Create pet care tasks with different times and recurrence options.
4. View the daily schedule, which is automatically sorted by time.
5. If two tasks are scheduled for the same time, the scheduler displays a conflict warning.
6. Mark a recurring task as complete to automatically generate the next daily or weekly task.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
