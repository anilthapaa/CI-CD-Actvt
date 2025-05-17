# employee_manager.py

class Employee:
    """A class representing an employee."""

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def apply_raise(self, percentage):
        """
        Apply a raise to the employee's salary.

        Args:
            percentage (float): The percentage increase (e.g., 10 for 10%).

        Raises:
            ValueError: If the percentage is negative.
        """
        if percentage < 0:
            raise ValueError("Raise percentage must be positive.")
        self.salary += self.salary * (percentage / 100)

    def get_annual_salary(self):
        """Return the annual salary."""
        return self.salary * 12

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}) earns ${self.salary:.2f}/month"
