class Employee:
    def __init__(self, emp_id, name, position, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.work_schedule = []

    def add_work_schedule(self, day, hours_worked):
        self.work_schedule.append({"day": day, "hours_worked": hours_worked})

    def get_total_hours_worked(self):
        return sum(schedule["hours_worked"] for schedule in self.work_schedule)

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}"
