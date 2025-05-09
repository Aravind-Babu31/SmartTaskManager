# AI-Based Task Manager Agent: SmartTaskMate

You can easily organize your daily tasks with the help of SmartTaskMate, an AI-powered task manager agent. When given natural language input, such as "Buy groceries tomorrow morning," it automatically extracts the task, day, time, and category and stores them in a database in an organized manner.


With the help of Google Gemini Pro, Streamlit, and SQLite, this tool uses intelligent language understanding to make task management easier.

---

## Characteristics

Accepts task descriptions in natural language. Automatically extracts structured information, including `task`, `day`, `time`, and `category`  
✅ Infers category even when it isn't mentioned directly (work, personal, shopping, etc.)  
✅ Tasks are stored in a tidy **SQLite database** 
✅ The codebase is of production quality and has a modular structure.
✅ For high accuracy, **few-shot prompting** with Gemini is used.

---

## Problem Description

It takes a lot of time and effort to manually enter structured task information. The majority of users favor using natural language when writing or speaking. This is resolved by SmartTaskMate, which lets users naturally describe tasks and then employs a generative AI agent to **understand and organize** them efficiently.

---
Project Structure :

SmartTaskMate/
├── .env                         # Environment variables (Google API key)
├── requirements.txt             # Python dependencies
├── taskmanager.db               # SQLite database
└── src/
    ├── streamlit_app.py         # Streamlit user interface
    ├── agents/
    │   └── task_parser.py       # Gemini-based task extraction
    └── utils/
        └── db.py                # Database handling
        
## Overview of the Architecture

```text
+-----------------------+
| Streamlit User Interface |   (User types a task) |
+----------+------------+
           |
           v
+---------------------+
| Gemini Task Parser |        |(extracts task information) |
+----------+-------------+
           |
           v
 +---------------------+
| SQLite Database ||           (task, day, time, etc.) |
+---------------------+
           |
           v
+---------------------+
Visual Task List ||            (Shows everything) |
+---------------------+



