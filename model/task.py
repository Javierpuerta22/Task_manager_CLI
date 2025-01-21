import datetime as dt
from termcolor import colored

class Task:
    def __init__(self, task_group, task_name, task_description, task_status, task_created:dt.datetime = None):
        self.task_group = task_group.capitalize()
        self.task_name = task_name.capitalize()
        self.task_description = task_description.capitalize()
        self.task_status = task_status.capitalize()
        self.task_created = dt.datetime.fromisoformat(task_created) if task_created else dt.datetime.now()
        self.task_status_color = {'To do': 'red', 'Doing': 'yellow', 'Done': 'green'}

    def __str__(self):
        return f"Task: {self.task_name} - {self.task_description} - {self.task_status} - {self.task_created.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def __repr__(self):
        return f"Task: {self.task_name} - {self.task_description} - {self.task_status} - {self.task_created.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def to_dict(self):
        return {
            'task_group': self.task_group,
            'task_name': self.task_name,
            'task_description': self.task_description,
            'task_status': self.task_status,
            'task_created': self.task_created.astimezone().isoformat()
        }
        
        
    def to_print(self, max_length:int):
        print(f"{self.task_group:<15} | {self.task_name:<20} | {self.task_description:<{max_length}} | {colored(self.task_status, self.task_status_color[self.task_status])} | {colored(self.task_created.strftime('%Y-%m-%d %H:%M:%S'), 'light_green'):<20} |")
    
