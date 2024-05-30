from src.data_model import *

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


def main():

    print_version = print_postgres_version()

    if print_version:
        print(PURPLE + ITALIC + f"\nDatabase server version:\n {print_version}" + RESET)
        print('\n')
    else:
        print(RED + BOLD + "Failed to retrieve the database version." + RESET)

     
    get_warehouse_detail(2)   

    get_employee_detail(105)

    update_employee_experience(101)

    get_specialist_employee_list("Driver", 30000)

    create_employee("INSERT INTO Employee (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience) \
      VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
    )


if __name__ == '__main__':
    main()