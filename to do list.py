import json
from datetime import datetime
from termcolor import colored
import pyfiglet
import inquirer

class ToDoList:
    file_path = "data.json"

    def __init__(self, name, desc, dateStart=None, status=False):
        self.name = name
        self.desc = desc
        self.dateStart = dateStart if dateStart else str(datetime.now().date())
        self.status = status

    def __str__(self) -> str:
        status_str = 'Completed' if self.status else 'Pending'
        return (f"Project: {self.name}\n"
                f"Description: {self.desc}\n"
                f"Start date: {self.dateStart}\n"
                f"Status: {status_str}")

    @staticmethod
    def _read_data():
        try:
            with open(ToDoList.file_path, "r") as json_file:
                return json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def loadTasks():
        data = ToDoList._read_data()
        return [ToDoList(**task) for task in data]

    def addTask(self):
        data = ToDoList._read_data()
        data.append(self.__dict__)
        try:
            with open(ToDoList.file_path, "w") as json_file:
                json.dump(data, json_file, indent=2)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(e)

    @staticmethod
    def removeTask(index):
        data = ToDoList._read_data()
        try:
            data.pop(index - 1)
            with open(ToDoList.file_path, "w") as json_file:
                json.dump(data, json_file, indent=2)
        except IndexError:
            print(f"Error: No task at index {index}")
        except Exception as e:
            print(e)

    @staticmethod
    def changeStatus(index, new_status):
        data = ToDoList._read_data()
        try:
            data[index - 1]['status'] = new_status
            with open(ToDoList.file_path, "w") as json_file:
                json.dump(data, json_file, indent=2)
        except IndexError:
            print(f"Error: No task at index {index}")
        except Exception as e:
            print(e)

def main_menu():
    while True:
        print(colored(pyfiglet.figlet_format("To-Do List"), "cyan"))
        questions = [
            inquirer.List(
                'choice',
                message="What do you want to do?",
                choices=[
                    'Add Task',
                    'View Tasks',
                    'Remove Task',
                    'Change Task Status',
                    'Exit'
                ],
            ),
        ]
        answer = inquirer.prompt(questions)['choice']
        
        if answer == 'Add Task':
            name = input(colored("Enter task name: ", "green"))
            desc = input(colored("Enter task description: ", "green"))
            task = ToDoList(name, desc)
            task.addTask()
            print(colored("Task added successfully.", "yellow"))
        
        elif answer == 'View Tasks':
            tasks = ToDoList.loadTasks()
            for index, task in enumerate(tasks, start=1):
                print(colored(f"\nTask {index}:\n{'-'*20}\n{task}\n{'-'*20}\n", "blue"))
        
        elif answer == 'Remove Task':
            index = int(input(colored("Enter the task index to remove: ", "red")))
            ToDoList.removeTask(index)
            print(colored("Task removed successfully.", "yellow"))
        
        elif answer == 'Change Task Status':
            index = int(input(colored("Enter the task index to change status: ", "red")))
            status = inquirer.prompt([inquirer.List('status', message="Enter new status", choices=['true', 'false'])])['status'] == 'true'
            ToDoList.changeStatus(index, status)
            print(colored("Task status updated successfully.", "yellow"))
        
        elif answer == 'Exit':
            print(colored("Exiting the program.", "red"))
            break
        
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main_menu()

