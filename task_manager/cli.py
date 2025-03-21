import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task Subcommand
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")
    parser_add.add_argument("--priority", type=int, default=1, help="Task priority (default: 1)")

    # List Tasks Subcommand
    subparsers.add_parser("list", help="List all tasks")

    # Delete Task Subcommand
    parser_delete = subparsers.add_parser("delete", help="Delete a task by its ID")
    parser_delete.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.description, args.priority)
        logger.info(f"Task added: {task}")
        print(f"Task added: {task}")
    elif args.command == "list":
        tasks = list_tasks()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")
    elif args.command == "delete":
        result = delete_task(args.task_id)
        if result:
            logger.info(f"Task {args.task_id} deleted.")
            print(f"Task {args.task_id} deleted.")
        else:
            logger.warning(f"Task {args.task_id} not found.")
            print(f"Task {args.task_id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
