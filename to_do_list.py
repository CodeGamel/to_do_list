from functions_ import add_task
from functions_ import view_tasks
from functions_ import mark_completed

to_do_list = {



}

def main():
   flag = True
   while flag :
        ans = input('''
 Welcome to the To-Do List App!


    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
''')
        if ans == '1': #write a function that adds a task
            add_task()
        if ans == '2': #write a function that views tasks
            view_tasks()
        if ans =='3': #write a function that marks a tasks complete
            mark_completed()
        if ans =='4' : #write a function that deletes a task
            pass
        if ans=='5':
            break


main()



def del_tasks():
    user_input = input("Which task would you like to delete?")
    