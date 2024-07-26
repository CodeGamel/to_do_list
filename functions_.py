to_do_list = {



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
    if not to_do_list:
        print("No tasks avaliable. \n")
    for task_id, task_reputation in to_do_list.items():
        print(f'Task ID {task_id}')
        print(f" Task: {task_reputation['task']}")
        print(f" Status: {task_reputation['status']}")
        print(f" Priority: {task_reputation['priority']}\n")
    

def del_tasks():
    user_input = input("Enter Task ID")
    try:
        task_id = int(user_input)
    except ValueError:
        print("Invalid Task ID. Please enter a number")
    if task_id in to_do_list:
        del to_do_list[task_id]
        print(f'Task ID {task_id} has been removed')
    else:
        print("This could not be found.")
 
def mark_completed():
    user_input = input('which task have you done?') #ask the user which task they've done
    try:
        task_status = int(user_input) #getting input for task
    except ValueError:
        print("Invalid input. Please enter a number") #user must enter number
    if task_status in to_do_list:
        if to_do_list[task_status]['status'] == 'incomplete': #If status is equal to incomplete 
             to_do_list[task_status]['status'] = 'Complete'
        print('This task has been marked as completed')    
    else:
        print('This task either doesnt exist or you\'ve completed')
   
  


