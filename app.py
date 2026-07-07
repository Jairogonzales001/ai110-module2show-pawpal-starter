import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.write("A simple pet care scheduling assistant.")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

st.subheader("Owner Information")
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

if st.button("Save owner"):
    st.session_state.owner.name = owner_name
    st.success("Owner saved.")

st.divider()

st.subheader("Add a Pet")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add pet"):
    if pet_name:
        new_pet = Pet(pet_name, species)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"{pet_name} was added.")
    else:
        st.warning("Please enter a pet name.")

if st.session_state.owner.pets:
    st.write("Current pets:")
    pet_rows = []
    for pet in st.session_state.owner.pets:
        pet_rows.append({"Name": pet.name, "Species": pet.species})
    st.table(pet_rows)
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Add a Task")

if st.session_state.owner.pets:
    selected_pet = st.selectbox(
        "Choose pet",
        [pet.name for pet in st.session_state.owner.pets]
    )

    task_description = st.text_input("Task description", value="Morning walk")
    task_time = st.text_input("Task time", value="08:00")
    frequency = st.selectbox("Frequency", ["one-time", "daily", "weekly"])

    if st.button("Add task"):
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet:
                pet.add_task(Task(task_description, task_time, frequency))
                st.success(f"Task added for {selected_pet}.")
else:
    st.info("Add a pet before creating tasks.")

st.divider()

st.subheader("Today's Schedule")

scheduler = Scheduler(st.session_state.owner)

if st.button("Generate schedule"):
    tasks = scheduler.sort_by_time()

    if tasks:
        schedule_rows = []

        for pet_name, task in tasks:
            schedule_rows.append(
                {
                    "Time": task.time,
                    "Pet": pet_name,
                    "Task": task.description,
                    "Frequency": task.frequency,
                    "Completed": task.completed,
                }
            )

        st.table(schedule_rows)

        conflicts = scheduler.detect_conflicts()

        if conflicts:
            for conflict in conflicts:
                st.warning(conflict)
        else:
            st.success("No scheduling conflicts found.")
    else:
        st.info("No tasks have been added yet.")