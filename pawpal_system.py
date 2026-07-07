from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "one-time"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def create_next_occurrence(self):
        """Create the next task if this is daily or weekly."""
        if self.frequency.lower() == "daily":
            return Task(self.description, self.time, self.frequency, self.due_date + timedelta(days=1))

        if self.frequency.lower() == "weekly":
            return Task(self.description, self.time, self.frequency, self.due_date + timedelta(days=7))

        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Get all tasks for all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))

        return all_tasks


class Scheduler:
    def __init__(self, owner):
        """Create a scheduler for an owner."""
        self.owner = owner

    def sort_by_time(self):
        """Sort all tasks by time."""
        return sorted(self.owner.get_all_tasks(), key=lambda item: item[1].time)

    def filter_by_pet(self, pet_name):
        """Return tasks for one pet."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if pet.lower() == pet_name.lower()
        ]

    def filter_by_status(self, completed):
        """Return tasks by completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def mark_task_complete(self, pet_name, task_description):
        """Complete a task and create the next recurring task if needed."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description.lower() == task_description.lower() and not task.completed:
                        task.mark_complete()

                        next_task = task.create_next_occurrence()
                        if next_task:
                            pet.add_task(next_task)

                        return True

        return False

    def detect_conflicts(self):
        """Check for tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for pet_name, task in self.owner.get_all_tasks():
            if task.time in seen_times:
                other_pet, other_task = seen_times[task.time]
                conflicts.append(
                    f"Conflict: {pet_name}'s task '{task.description}' is at the same time as "
                    f"{other_pet}'s task '{other_task.description}' at {task.time}."
                )
            else:
                seen_times[task.time] = (pet_name, task)

        return conflicts