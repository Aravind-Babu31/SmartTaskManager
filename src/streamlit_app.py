import streamlit as st
from agents.task_parser import extract_task_details
from utils.db import insert_task, fetch_tasks

st.set_page_config(page_title="SmartTaskMate", layout="centered")
st.title(" SmartTaskMate")
st.write("Organize your tasks using SmartTaskmate AI ")

# Input box for user to enter a task
user_input = st.text_input("Enter your task:")

if st.button("Add Task"):
    if user_input:
        with st.spinner("Analyzing with SmartTaskMate AI..."):
            result = extract_task_details(user_input)
        if result:
            insert_task(result["task"], result["day"], result["time"], result["category"])
            st.success("✅ Task added!")
        else:
            st.error("⚠️ Sorry, I couldn't understand that.")
    else:
        st.warning("Please enter a task first.")

# Display all tasks
st.subheader("📋 Your Task List")
tasks = fetch_tasks()
if tasks:
    for t in tasks:
         day_display = t[2] if t[2] else "Not specified"
         time_display = t[3] if t[3] else "Not specified"
         st.markdown(f"**{t[0]}. {t[1]}**  \n📅 {day_display} 🕒 {time_display} | 📂 {t[4]}")


else:
    st.info("No tasks added yet.")

