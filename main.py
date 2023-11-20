import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="zXrnKK6WNV",
    password="asdf"
)

def create_database():
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS employee")
    con.commit()
    cursor.close()

def create_table():
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee.Employees (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            job_title VARCHAR(255),
            salary INT
        )
    ''')
    con.commit()
    cursor.close()

def Add_Employ():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Try Again.")
        menu()
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
        data = (Id, Name, Post, Salary)
        sql = 'INSERT INTO employee.Employees VALUES (%s, %s, %s, %s)'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully ")
        menu()

def Promote_Employee():
    Id = input("Enter Employee's Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Try Again.")
        menu()
    else:
        Amount = int(input("Enter increase in Salary: "))
        sql_select = 'SELECT salary FROM employee.Employees WHERE employee_id=%s'
        data_select = (Id,)
        cursor = con.cursor()
        cursor.execute(sql_select, data_select)
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount
        sql_update = 'UPDATE employee.Employees SET salary=%s WHERE employee_id=%s'
        data_update = (new_salary, Id)
        cursor.execute(sql_update, data_update)
        con.commit()
        print("Employee Promoted")
        menu()

def Remove_Employ():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Try Again.")
        menu()
    else:
        sql = 'DELETE FROM employee.Employees WHERE employee_id=%s'
        data = (Id,)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed")
        menu()

def check_employee(employee_id):
    sql = 'SELECT * FROM employee.Employees WHERE employee_id=%s'
    cursor = con.cursor(buffered=True)
    data = (employee_id,)
    cursor.execute(sql, data)
    return cursor.rowcount == 1

def Display_Employees():
    sql = 'SELECT * FROM employee.Employees'
    cursor = con.cursor()
    cursor.execute(sql)
    employees = cursor.fetchall()
    for employee in employees:
        print("Employee Id:", employee[0])
        print("Employee Name:", employee[1])
        print("Employee Post:", employee[2])
        print("Employee Salary:", employee[3])
        print("---------------------" * 4)
    menu()

def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

# Call the create_database function
create_database()

# Connect to the 'employee' database
con.database = 'employee'

# Call the create_table function
create_table()

# Calling menu function
menu()
