from employees.employee import Employee
from employees.employee_manager import EmployeeManager
from employees.database import create_database

def main():
    conn = create_database()
    employee_manager = EmployeeManager(conn)

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Calculate Payroll")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            hourly_rate = float(input("Enter employee hourly rate: "))

            employee = Employee(None, name, position, hourly_rate)
            employee_manager.add_employee(employee)
            print("Employee added successfully!")

        elif choice == "2":
            emp_id = int(input("Enter employee ID: "))
            employee = employee_manager.find_employee_by_id(emp_id)
            if employee:
                print(f"Employee Details:\n{employee}")
            else:
                print("Employee not found.")

        elif choice == "3":
            total_payroll = employee_manager.calculate_total_payroll()
            print(f"Total Payroll: ${total_payroll:.2f}")

        elif choice == "4":
            break

        if __name__ == "__main__":
    main()
