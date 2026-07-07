from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "one-time"
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass


@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self):
        pass

    def filter_by_pet(self, pet_name):
        pass

    def filter_by_status(self, completed):
        pass

    def mark_task_complete(self, pet_name, task_description):
        pass

    def detect_conflicts(self):
        pass