from datetime import *




def menu():
    print("Enter the number that corresponds to the menu option. Press q to exit.")
    print("1. Create Planner")
    print("2. Load Planner")
    
    selection = input()

    if selection == '1':
        create_planner()
    elif selection == '2':
        file_name = input("Please input the date of the planner you would like to load.\nWeekday/Day/Month/Year: ")
        load_planner(file_name)

def create_planner():

    f = open(get_date(),'w')

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

    display_lines(get_date())

    f.write(get_date() + '\n')

    task_list = sorted(task_list)

    for i in range(len(task_list)):
        print(task_list[i][0] + ' ' + task_list[i][1])
        f.write(task_list[i][0] + ' ' + task_list[i][1] + '\n')


def load_planner(file_name):
    f = open(file_name,'r')
    
    display_lines(f.readline().strip())

    line = f.readline().strip()
    print(line)

    while line:
        line = f.readline().strip()
        print(line)


def get_date():
    now = datetime.today()
    date = now.strftime('%A %d %B %Y')
    date = date
    return date

def display_lines(text):
    print('-'*50)
    print('-'*50)
    print(text.center(50))
    print('-'*50)
    print('-'*50)
    
if __name__ == "__main__":
    title = "Daily Planner"
    display_lines(title)
    menu()
