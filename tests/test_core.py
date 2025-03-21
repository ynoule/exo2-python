import os
import json
import unittest
from task_manager.core import add_task, delete_task, load_tasks, save_tasks

TEST_TASKS_FILE = "test_tasks.json"

# Override the TASKS_FILE path in the core module for testing
import task_manager.core
task_manager.core.TASKS_FILE = TEST_TASKS_FILE

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Ensure a fresh test file before each test
        with open(TEST_TASKS_FILE, "w") as f:
            json.dump([], f)

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(TEST_TASKS_FILE):
            os.remove(TEST_TASKS_FILE)

    def test_add_task(self):
        task = add_task("Test task", 2)
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["priority"], 2)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], task["id"])

    def test_delete_task(self):
        # Add two tasks
        task1 = add_task("Task to delete", 1)
        task2 = add_task("Task to keep", 1)
        # Delete task1
        result = delete_task(task1["id"])
        self.assertTrue(result)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], task2["id"])
        # Try to delete a non-existing task
        result = delete_task(999)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
