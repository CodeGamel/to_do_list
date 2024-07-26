to_do_list = {
1: {'task': '', "status": "incomplete", "priority": ""},
2: {'task': ''  , "status": '', "priority" : ''},
3: {'task': '', "status": '', "priority": ''},
}

def add_task():
    user_input = input("Add your task now.") #collecting input
    task_id = len(to_do_list) +1 #generates taskID
    priority_input = input('How important is this task? 1 - Important 2 - Not too important 3 - Not at all') #input chooses priority
    if priority_input == '1':
        priority = 'Important'
    elif priority_input == '2':
        priority = 'Not too important'   
    elif priority_input == '3':
       priority = 'Not at all'
    else:
        print('Invalid Option') #They must return a value
        return
    to_do_list[task_id] =   {
        'task': user_input,
        'status': 'incomplete',
        'priority': priority
    }
    print(f"Task ID {task_id}: '{user_input}' with priority '{priority}' has been added to your task list")

def view_tasks():
    for task_id, task_status in to_do_list.items():
        print(f'Task ID {task_id}')
        print(f" Task: {task_status['task']}")
        print(f" Status: {task_status['status']}")
        print(f" Priority: {task_status['priority']}\n")

def del_tasks():
    user_input = input("Which task would you like to delete?")
    for task in to_do_list:
        if input == task:
            del(task)
            print(f'{task} has been removed')
 
def mark_completed():
    for taskstatus in to_do_list:
     if taskstatus == 'Not Finished':
        input('which task have you done?')
        if input == taskstatus:
            print(f"This {to_do_list} is now finished. Good Job!")

