import mysql.connector as conn
import re
from tabulate import tabulate

db_ref = conn.connect(host="localhost",user="root",passwd="12345")
cursor_1 = db_ref.cursor()
cursor_1.execute("CREATE DATABASE IF NOT EXISTS todolist")
cursor_1.execute("USE todolist")
cursor_1.execute("""CREATE TABLE IF NOT EXISTS main_table(
                 task_name varchar(255) NOT NULL primary key,
                 task_time varchar(255) NOT NULL,
                 task_record varchar(255) NOT NULL)""")
print("HELLO USER \n PLEASE SELECT ONE OF THE FOLLOWING COMMANDS TO PROCEED FURTHUR\n\t1.VIEW TASKS\n\t2.ADD TASKS\n\t3.UPDATE TASK\n\t4.DELETE TASK\n\t5.CHANGE STATUS\n\t6.EXIT")
while True:
    user_inp = int(input())
    if (user_inp==1):
        cursor_1.execute("SELECT * FROM main_table")
        data = cursor_1.fetchall()
        data.insert(0,("TASK NAME","TASK TIME","STATUS"))
        if (data):
            print(tabulate(data))
            print("\nRECORDED TASKS SUCCESSFULLY DISPLAYED")
        else:
            print("No records found ,please add a task to get started")
    elif (user_inp==2):
        task_name = input("Enter the task name : ")
        task_time = input("Enter the time scheduled for the above mentioned activity : ")
        cursor_1.execute("SELECT task_name FROM main_table")
        data = cursor_1.fetchall()
        if task_name not in data and re.match("^[0-9][0-9]:[0-9][0-9]$",task_time):
            cursor_1.execute(f"INSERT INTO main_table VALUES ('{task_name.lower()}','{task_time}','not done')")
            print("RECORD SUCCESSFULLY ADDED TO THE TABLE")
        else:
            print("INVALID ENTRY ,THE NAME ALREADY EXISTS OR THE TIME FORMAT IS WRONG. PLEASE ENTER A VALID ONE.")

    elif (user_inp == 3):
        task_name = input("Enter the task name : ").lower()
        cursor_1.execute("SELECT task_name FROM main_table")
        task_list = [i[0] for i in cursor_1.fetchall()]
        if task_name in task_list:
            new_name = input("Enter the new task name : ")
            new_time = input("Enter the new time : ")
            if new_name not in task_list and re.match("^[0-9][0-9]:[0:9][0:9]$",new_time):
                cursor_1.execute(f"UPDATE main_table SET task_name = '{new_name}', task_time = '{task_time}' WHERE task_name='{task_name}'")
                print("TASK RECORD UPDATED SUCCESSFULLY")
            else:
                print("A TASK WITH THAT NAME ALREADY EXISTS")
        else:
            print("INVALID TASK INPUT ,PLEASE ENTER A VALID ONE.")
    elif (user_inp==4):
        task_name = input("Enter name of the task to be deleted : ")
        cursor_1.execute("SELECT task_name FROM main_table")
        data_1 = [i[0] for i in cursor_1.fetchall()]
        if task_name in data_1:
            cursor_1.execute(f"DELETE FROM main_table WHERE task_name='{task_name}'")
            print(f"{task_name} successfully deleted")
        else:
            print("INVALID TASK ENTRY")
    elif (user_inp==5):
        task_name = input("Enter the name of task : ")
        cursor_1.execute(f"SELECT * FROM main_table WHERE task_name='{task_name}'")
        data_2 = cursor_1.fetchall()
        if (data_2):
            if (data_2[0][2]=="not done"):
                cursor_1.execute(f"UPDATE main_table SET task_record = 'done' WHERE task_name='{task_name}'")
            else:
                cursor_1.execute(f"UPDATE main_table SET task_record = 'not done' WHERE task_name='{task_name}'")
            print("STATUS RECORD SUCCESSFULLY UPDATED !!!")
        else:
            print("THE REQUESTED TASK WAS NOT FOUND. PLEASE ENTER A VALID ONE")
    elif (user_inp==6):
        break
    else:
        print("INVALID INPUT ,PLEASE ENTER A VALID ONE")
    print("PLEASE SELECT ONE OF THE FOLLOWING COMMANDS TO PROCEED FURTHUR\n\t1.VIEW TASKS\n\t2.ADD TASKS\n\t3.UPDATE TASK\n\t4.DELETE TASK\n\t5.CHANGE STATUS\n\t6.EXIT")
print("THANK YOU")
db_ref.commit()
cursor_1.close()
db_ref.close()