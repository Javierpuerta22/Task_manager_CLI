import cmd, os, json, shlex
from model.task import Task

class Interface(cmd.Cmd):
    prompt = 'Task Manager >>> '
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
        
        
        
        filtered_task_list = self.task_list['tasks'] if not line else [task for task in self.task_list['tasks'] if task['task_group'].find(line) != -1]
        
        max_length = max(map(lambda task: len(task['task_description']), filtered_task_list))
        
        max_length = max(max_length, 30)
        
        num_iguales = 103 + (max_length - 30)
        
        print("="*num_iguales)
        print(f"{'Group':<15} | {'Name':<20} | {'Description':<{max_length}} | {'Status':<6} | {'Created':<18} |")
        
        for task in filtered_task_list:
            print("-"*num_iguales)
            Task(**task).to_print(max_length)
        
        print("="*num_iguales)

    
    def do_add(self, line):
        """Add a task."""
        # we make a map of the task attributes from the input line
        line = shlex.split(line)
        self.task_list['tasks'].append(Task(*line).to_dict())
        
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            
    def do_done(self, line):
        """Mark a task as done."""
        task_name = line.capitalize()
        task = next(filter(lambda task: task['task_name'] == task_name, self.task_list['tasks']), None)
                
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            
            
    def do_delete(self, line:str):
        """Delete a task."""
        task_name = line.capitalize()
        self.task_list['tasks'] = list(filter(lambda task: task['task_name'] != task_name, self.task_list['tasks']))
        
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            
            
    def do_doing(self, line):
        """Mark a task as doing."""
        task_name = line.capitalize()
        task = next(filter(lambda task: task['task_name'] == task_name, self.task_list['tasks']), None)
        
        # we update the task status to 'Doing'
        task['task_status'] = 'Doing'
        
        # we update the task in the task list
        for i, t in enumerate(self.task_list['tasks']):
            if t['task_name'] == task_name:
                self.task_list['tasks'][i] = task
                break
    
                
        with open('data/task_list.json', 'w') as file:
            json.dump(self.task_list, file)
            

    def do_exit(self, line):
        """Exit the CLI."""
        return True
    