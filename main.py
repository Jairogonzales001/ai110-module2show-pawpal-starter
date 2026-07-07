from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Jairo")

dog = Pet("Max", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Morning walk", "08:00", "daily"))
dog.add_task(Task("Vet appointment", "14:00", "one-time"))
cat.add_task(Task("Feed Luna", "07:30", "daily"))
cat.add_task(Task("Clean litter box", "08:00", "daily"))

scheduler = Scheduler(owner)

print("Today's Schedule")
print("----------------")

for pet_name, task in scheduler.sort_by_time():
    print(f"{task.time} - {pet_name}: {task.description} ({task.frequency})")

print("\nConflict Warnings")
print("-----------------")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for conflict in conflicts:
        print(conflict)
else:
    print("No conflicts found.")