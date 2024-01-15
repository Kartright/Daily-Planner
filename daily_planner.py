from datetime import *


def menu():
    display_lines("Daily Planner")
    print("Enter the number that corresponds to the menu option. Press q to exit.")
    print("1. Create Planner")
    print("2. Load Planner")
    print("3. Edit Planner")
    
    selection = input()

    if selection != 'q':
        if selection == '1':
            create_planner()
            menu()
        elif selection == '2':
            file_name = input("Please input the date of the planner you would like to load.\nDay/Month/Year: ")
            load_planner(file_name)
            menu()
        elif selection == '3':
            file_name = input("Please input the date of the planner you would like to edit.\nDay/Month/Year: ")
            edit_planner(file_name)
            menu()
    pass


def create_planner():

    day = input("In how many days is the desired date from todays date? (Type 0 for todays date)\n")

    f = open(get_date(day),'w')

    print("Begin by typing the task. Type 'exit' to stop adding tasks and display planner.")
    task_list = []
    task = input("Please input the task: ")

    # ask for task inputs until user inputs exit
    while task != 'exit':
        single_task_list = []
        task_time = input("Please input the time of the task: ")
        single_task_list.append(task_time)
        single_task_list.append(task)
        task_list.append(single_task_list)
        task = input("Please input the next task: ")

    display_lines(get_date(day))

    f.write(get_date(day) + '\n')

    task_list = sorted(task_list)

    for i in range(len(task_list)):
        print(task_list[i][0] + ' ' + task_list[i][1])
        f.write(task_list[i][0] + ' ' + task_list[i][1] + '\n')
    
    f.close


def load_planner(file_name):
    f = open(file_name,'r')
    
    display_lines(f.readline().strip())

    line = f.readline().strip()
    print(line)

    while line:
        line = f.readline().strip()
        print(line)
    
    f.close


def edit_planner(file_name):

    f = open(file_name, 'r')

    day = f.readline()

    task_list = []

    line = f.readline().strip()

    while line:
        task_list.append(line.split(" ",1))
        line = f.readline().strip()

    f.close

    w = open(file_name,'w')

    print("Begin by typing the task. Type 'exit' to stop adding tasks and display planner.")
    task = input("Please input the task: ")

    # ask for task inputs until user inputs exit
    while task != 'exit':
        single_task_list = []
        task_time = input("Please input the time of the task: ")
        single_task_list.append(task_time)
        single_task_list.append(task)
        task_list.append(single_task_list)
        task = input("Please input the next task: ")

    task_list = sorted(task_list)

    display_lines(day.strip())
    w.write(day)

    for i in range(len(task_list)):
        print(task_list[i][0] + ' ' + task_list[i][1])
        w.write(task_list[i][0] + ' ' + task_list[i][1] + '\n')
    
    w.close


def get_date(num_of_days):
    now = datetime.today() + timedelta(days=int(num_of_days))
    date = now.strftime('%d %B %Y')
    date = date
    return date


def display_lines(text):
    print('-'*50)
    print('-'*50)
    print(text.center(50))
    print('-'*50)
    print('-'*50)
    

if __name__ == "__main__":
    menu()
