from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Feed dog", "08:00")
    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Max", "Dog")
    task = Task("Walk", "09:00")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sorting_correctness():
    owner = Owner("Jairo")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Night walk", "20:00"))
    pet.add_task(Task("Morning walk", "08:00"))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0][1].description == "Morning walk"


def test_daily_recurrence():
    owner = Owner("Jairo")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    task = Task("Feed dog", "08:00", "daily", date.today())
    pet.add_task(task)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete("Max", "Feed dog")

    assert len(pet.tasks) == 2
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    owner = Owner("Jairo")
    dog = Pet("Max", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Walk", "08:00"))
    cat.add_task(Task("Feed", "08:00"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1