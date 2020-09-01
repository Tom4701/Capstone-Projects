# This program helps a small business to manage tasks and users to keep track of their various assignments
import datetime

# User option menu:
r = "r \t - register user"
a = "a \t - add task"
va = "va \t - view all my tasks"
vm = "vm \t - view my tasks"
e = "e \t - exit"

username = False
password = False
result = ""

# Counter desk
user_count = 1
task_count = 2
my_2d_list = []

user_file = open("user.txt", "r+")

data = user_file.readlines()
    #f.close()
print(user_file.readline())
for item in data:
        print(item)

for line in user_file:
    line = line.replace("\n", "")
    my_list = line.split(", ")
    my_2d_list.append(my_list)

username_check = False
pass_check = False

while (username_check == False) or (pass_check == False):

    username = input("Enter Username: ")
    
    for group in my_2d_list:
        if group[0] == username:
            
            username_check = True 
            password = input("Please enter password: ")
            result = "Logged in!"
            pass_check = True
            if password == group[1]:
                result = "Username correct, password incorrect"

            else:
                username_check = False
                pass_check = False
                result = "Username is correct, Password is incorrect!"
        else:
            username_check = False
            pass_check = False
            result = "Username is incorrect!"

    password = input("Enter Password: ")
    if line == username + ", " + password + "\n":
        menu_option = input(f"Welcome! Please make your selection below: \n {r}\n {a}\n {va}\n {vm}\n {e}\n").lower()
            
        if menu_option == "r" and username == "admin":  # The 'register user' option is only available to admin
            username = input("Enter new user name: \n")
            password = input("Enter user's password: \n")
            confirm = input("Please confirm password: \n")
            user_count +=1
            if password != confirm:
                print("Passwords don't match, re-enter password") # If passwords don't match, admin would have to retry
                print(confirm)
    
            else:
                user_det = (username + ", " + password)
                out_file = open("user.txt", "a")  # The new user details are added to user details
                out_file.write(user_det+"\n")
                out_file.close()
                print(" New user added!")


        if menu_option == "a":  # When 'add task' option is chosen, user will have to add task details as below
            print("Please enter the following task details ")
            username = input("Enter user name: \n")
            task_title = input("Enter the title of task: \n")
            task_count +=1
            task_descr = input("Describe the task to be assigned: \n")
            date_assigned = datetime.date.today()  # Date of assignment is set by default to current date
            due_date = input("Enter the due date: \n")
            complete = False  # Task is set to not complete by default
            if complete == False:
                complete = "No"
            else:
                complete = "Yes"
            assign = (username + ", " + task_title + ", "+ task_descr + ", " + str(date_assigned) + ", " + due_date + ", " + complete)
            out_file = open("tasks.txt", "a")
            out_file.write(assign+"\n") # Task information including user to whom it's assigned is stored in 'tasks.txt' file
            out_file.close()


        if menu_option == "va": # When the 'view all' option is chosen, the user can see all the tasks and their respectie description on the screen
            view_all = ""
            with open("tasks.txt", "rt") as f:
                for line in f:
                    view_all = line.split(",")
                    view_all += line
                    print(view_all[1:3])

        if menu_option == "vm": # when the 'view my tasks' option is chosen, a user will be able to see only the tasks assigned to them
            with open("tasks.txt","r") as f:
                for line in f:
                    name, task, description, date, duedate, complete = line.split(",")
                    name = input("Enter your username: ") # This allows one to enter their user name in order to display only the tasks assigned to them
                    print(f" User {name} is assigned with task {task}: {description}")
                    if username == "admin":
                        print(f"The number of users is {user_count}. Total number of tasks is {task_count}")

        if menu_option == "e":
            exit()

    else:
        print("Incorrect login details")

user_file.close()