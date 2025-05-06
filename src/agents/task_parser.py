import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")

SYSTEM_PROMPT = """
You are a smart task assistant. Your job is to extract structured information from a natural language task.

From the user input, extract:
- "task": a short description of the task
- "day": the date or weekday mentioned (e.g., "tomorrow", "Monday", "next Friday")
- "time": time of day if mentioned (e.g., "3pm", "14:00", "morning")
- "category": one of ["work", "personal", "shopping", "health", "others"] based on the content, even if not explicitly mentioned.

If any field is not present in the input, leave it as null.

Respond only in JSON format as:
{
  "task": "...",
  "day": "...",
  "time": "...",
  "category": "..."
}

Examples:

Input: "Schedule a meeting with John next Friday at 3pm"
Output: {
  "task": "Schedule a meeting with John",
  "day": "next Friday",
  "time": "3pm",
  "category": "work"
}

Input: "Buy groceries this Saturday morning"
Output: {
  "task": "Buy groceries",
  "day": "this Saturday",
  "time": "morning",
  "category": "shopping"
}

Input: "Visit the doctor tomorrow at 9am"
Output: {
  "task": "Visit the doctor",
  "day": "tomorrow",
  "time": "9am",
  "category": "health"
}

Input: "Submit final project report by Tuesday"
Output: {
  "task": "Submit final project report",
  "day": "Tuesday",
  "time": null,
  "category": "work"
}

Input: "Call mom tonight"
Output: {
  "task": "Call mom",
  "day": "tonight",
  "time": null,
  "category": "personal"
}

"""

def extract_task_details(user_input):
    try:
        response = model.generate_content([
            SYSTEM_PROMPT,
            f"User: {user_input}"
        ])
        text = response.text.strip()

        # Safely parse response
        import json
        json_start = text.find("{")
        json_end = text.rfind("}")
        if json_start != -1 and json_end != -1:
            json_str = text[json_start:json_end+1]
            result = json.loads(json_str)

            return {
                "task": result.get("task"),
                "day": result.get("day"),
                "time": result.get("time"),
                "category": result.get("category")
            }
        return None
    except Exception as e:
        print("Parsing error:", e)
        return None
