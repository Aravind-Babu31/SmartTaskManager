from agents.task_parser import extract_task_details
from utils.db import insert_task, fetch_tasks


def main():
    print("🧠 Welcome to SmartTaskMate!")
    while True:
        user_input = input("\n📝 Enter your task (or 'view' or 'exit'): ")

        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "view":
            tasks = fetch_tasks()
            print("\n📋 Your Tasks:")
            for t in tasks:
                print(f"{t[0]}. {t[1]} | Date: {t[2]} | Category: {t[3]}")
        else:
            print("⏳ Thinking...")
            result = extract_task_details(user_input)
            if result:
                insert_task(result["task"], result["date"], result["category"])
                print("✅ Task added successfully!")
            else:
                print("⚠️ Couldn’t understand the task.")

if __name__ == "__main__":
    main()
