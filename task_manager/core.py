import json
import os
from task_manager.logger import setup_logger

logger = setup_logger()
TASKS_FILE = os.getenv("TASKS_FILE_PATH", "tasks.json")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            logger.debug("Loaded tasks successfully.")
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        logger.debug("No existing tasks found. Starting fresh.")
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
    logger.debug("Tasks saved.")

def add_task(description, priority):
    tasks = load_tasks()
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Task added: {task}")
    return task

def list_tasks():
    return load_tasks()

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        logger.warning(f"Task with ID {task_id} not found.")
        return False  # No task deleted
    save_tasks(new_tasks)
    logger.info(f"Task with ID {task_id} deleted.")
    return True
