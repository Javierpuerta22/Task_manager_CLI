import cmd, os, json, shlex
from model.task import Task

class Interface(cmd.Cmd):
    prompt = '>>> Task Manager / '
    intro = 'Welcome to the task manager interface!'
    
    def __init__(self):
        super().__init__()
        
        # Initialize the task list if it doesnt exist the file task_list.json in the data folder
        if not os.path.exists('data/task_list.json'):
            with open('data/task_list.json', 'w') as file:
                file.write('{"tasks": []}')
                
        # Load the task list from the file task_list.json
        with open('data/task_list.json', 'r') as file:
            self.task_list = json.load(file)
            
        self.actual_path = []
            
    
    def do_list(self, line):
        """List all tasks."""
        
        print("="*103)
        print(f"{'Group':<15} | {'Name':<20} | {'Description':<30} | {'Status':<6} | {'Created':<18} |")
        
        filtered_task_list = self.task_list['tasks'] if not line else [task for task in self.task_list['tasks'] if task['task_group'].find(line) != -1]
        
        for task in filtered_task_list:
            print("-"*103)
            Task(**task).to_print()
        
        print("="*103)

    
    def do_add(self, line):
        """Add a task."""
        # we make a map of the task attributes from the input line
        line = shlex.split(line)
        self.task_list['tasks'].append(Task(*line).to_dict())
        
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            
    def do_done(self, line):
        """Mark a task as done."""
        task_name = line
        task = next(filter(lambda task: task['task_name'] == task_name, self.task_list['tasks']), None)
                
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            
                
        
    
    
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_exit(self, line):
        """Exit the CLI."""
        return True
    