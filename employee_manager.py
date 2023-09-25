class EmployeeManager:
    def __init__(self, conn):
        self.conn = conn

    def add_employee(self, employee):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO employees (name, position, hourly_rate) VALUES (?, ?, ?)",
                    (employee.name, employee.position, employee.hourly_rate))
        employee.emp_id = cursor.lastrowid
        self.conn.commit()

    def find_employee_by_id(self, emp_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
        row = cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3])
        else:
            return None

    def calculate_total_payroll(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT hourly_rate FROM employees")
        rates = cursor.fetchall()
        total_payroll = sum(rate[0] for rate in rates)
        return total_payroll
