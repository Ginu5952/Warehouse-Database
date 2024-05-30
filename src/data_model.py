import psycopg2
from psycopg2 import pool
from datetime import date
from dateutil.relativedelta import relativedelta


# Colors

RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'

# Font Styles

BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'


try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        dbname="dci_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    if connection_pool:
        print(YELLOW + ITALIC + "\nConnection pool created successfully" + RESET)

except Exception as error:
    print(RED + BOLD + f"Error: {error}" + RESET)



def print_postgres_version() -> str:
     
    try:
        # Get connection from pool
        with connection_pool.getconn() as conn:
            with conn.cursor() as cursor:   
                
                # Execute the query to get the database version
                cursor.execute("SELECT version();")

                # Fetch the result
                db_version = cursor.fetchone()

                # Return the database version
                return db_version[0]

    except Exception as error:
        print(RED + BOLD + f"Error: {error}" + RESET)
        return None
    
    finally:
        if conn:
            connection_pool.putconn(conn)


def get_warehouse_detail(warehouse_id):

    conn = None
    cur = None

    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()

        with cur as cursor:

            cursor.execute("SELECT * FROM Warehouse WHERE warehouse_id = %s;", (warehouse_id,))
            warehouse_info = cursor.fetchall()

            if warehouse_info:

                print(YELLOW + ITALIC + "\nPrinting Warehouse record" + RESET)

                for warehouse in warehouse_info:
                        print(PURPLE + ITALIC + f"Warehouse Id: {warehouse[0]}" + RESET)
                        print(PURPLE + ITALIC + f"Warehouse Name: {warehouse[1]}" + RESET)
                        print(PURPLE + ITALIC + f"Employee Count: {warehouse[2]}" + RESET)
                        print('\n')
            else:
                # ID does not exist
                print(RED + BOLD + f"No warehouse found with id {warehouse_id}." + RESET)

    except Exception as error:
        print(RED + BOLD + f"Error: {error}" + RESET)      
    finally:
        if conn:
            connection_pool.putconn(conn)    

def get_employee_detail(employee_id):

    conn = None
    cur = None

    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()

        with cur as cursor:

            cursor.execute("SELECT * FROM Employee WHERE Employee_Id = %s;", (employee_id,))
            employee_info = cursor.fetchall()

            if employee_info:
                
                print(YELLOW + ITALIC + "\nPrinting Employee record" + RESET)

                for employee in employee_info:
                        
                        print(PURPLE + ITALIC + f"Employee Id: {employee[0]}" + RESET)
                        print(PURPLE + ITALIC + f"Employee Name: {employee[1]}" + RESET)
                        print(PURPLE + ITALIC + f"Warehouse Id: {employee[2]}" + RESET)
                        print(PURPLE + ITALIC + f"Joining Date: {employee[3]}" + RESET)
                        print(PURPLE + ITALIC + f"Speciality: {employee[4]}" + RESET)
                        print(PURPLE + ITALIC + f"Salary: {employee[5]}" + RESET)
                        print(PURPLE + ITALIC + f"Experience: {employee[6]}" + RESET)
                        print('\n')
            else:
                # ID does not exist
                print(RED + BOLD + f"No employee found with id {employee_id}." + RESET)

    except Exception as error:
        print(RED + BOLD + f"Error: {error}" + RESET)
            
    finally:
        if conn:
            connection_pool.putconn(conn)    


def update_employee_experience(employee_id):
           
    conn = None
    cur = None
    today = date.today()


    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()

        with cur as cursor:

            cursor.execute("SELECT Joining_Date FROM Employee WHERE Employee_Id = %s;", (employee_id,))
            joining_Date = cursor.fetchone()
            experience = relativedelta(today, joining_Date[0]).years
            
            cur.execute("UPDATE Employee SET Experience = %s WHERE Employee_Id = %s;", (experience, employee_id))
            conn.commit()

            cur.execute("SELECT * FROM Employee WHERE Employee_Id = %s;", (employee_id,))
            employee_info = cursor.fetchall()

            if employee_info:
                
                print(YELLOW + ITALIC + "\nPrinting Employee record" + RESET)

                for employee in employee_info:
                        
                    print(PURPLE + ITALIC + f"Employee Id: {employee[0]}" + RESET)
                    print(PURPLE + ITALIC + f"Employee Name: {employee[1]}" + RESET)
                    print(PURPLE + ITALIC + f"Warehouse Id: {employee[2]}" + RESET)
                    print(PURPLE + ITALIC + f"Joining Date: {employee[3]}" + RESET)
                    print(PURPLE + ITALIC + f"Speciality: {employee[4]}" + RESET)
                    print(PURPLE + ITALIC + f"Salary: {employee[5]}" + RESET)
                    print(PURPLE + ITALIC + f"Experience: {employee[6]}" + RESET)
                    print('\n')

            else:
                # ID does not exist
                print(RED + BOLD + f"No employee found with id {employee_id}." + RESET)  

    except Exception as error:
        print(RED + BOLD + f"Error: {error}" + RESET)

    finally:
        if conn:
            connection_pool.putconn(conn)    


def get_specialist_employee_list(speciality, salary):
   
    conn = None
    cur = None
  

    try:
        conn = connection_pool.getconn()
        cur = conn.cursor()

        with cur as cursor:

            cursor.execute("SELECT * FROM Employee WHERE Speciality = %s  AND Salary >= %s", (speciality, salary))
            get_list = cursor.fetchall()
            

            if get_list:
                
                print(YELLOW + ITALIC + "\nPrinting employees whose specialty is Driver and salary greater than 30000" + RESET)

                for item in get_list:
                        
                    print(PURPLE + ITALIC + f"Employee Id: {item[0]}" + RESET)
                    print(PURPLE + ITALIC + f"Employee Name: {item[1]}" + RESET)
                    print(PURPLE + ITALIC + f"Warehouse Id: {item[2]}" + RESET)
                    print(PURPLE + ITALIC + f"Joining Date: {item[3]}" + RESET)
                    print(PURPLE + ITALIC + f"Speciality: {item[4]}" + RESET)
                    print(PURPLE + ITALIC + f"Salary: {item[5]}" + RESET)
                    print(PURPLE + ITALIC + f"Experience: {item[6]}" + RESET)
                    print('\n')

            else:
                # ID does not exist
                print(RED + BOLD + f"No employee found with speciality {speciality} and salary {salary}" + RESET)  


    except Exception as error:
        print(RED + BOLD + f"Error: {error}" + RESET)

    finally:
        if conn:
            connection_pool.putconn(conn)        

def create_employee(employeeSqlQuery):

    conn = None
    cur = None

    try:
        
        employeeSqlQueryy =  employeeSqlQuery.rstrip(';') + " ON CONFLICT (Employee_Id) DO NOTHING;"

        conn = connection_pool.getconn()
        cur = conn.cursor()
       
        with cur as cursor:

            
            cursor.execute(employeeSqlQueryy)
            conn.commit() 

            cur.execute("SELECT * FROM Employee;")
            rows = cur.fetchall()

            if rows:
                print(YELLOW + ITALIC + "\nEmployee table:" + RESET)
                for row in rows:
                    print(PURPLE + ITALIC + f'{row}' + RESET)
            else:
                print(RED + BOLD + "\nNo employees found." + RESET)

        print(YELLOW + ITALIC + "\nEmployee created successfully." + RESET)

    except Exception as e:
        
        print(f"Error creating employee: {e}")   

    finally:
        if conn:
            connection_pool.putconn(conn)       