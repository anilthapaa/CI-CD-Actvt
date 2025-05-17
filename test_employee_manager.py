# test_employee_manager.py

import pytest
from employee_manager import Employee

def test_apply_raise():
    emp = Employee(1, "Alice", 5000)
    emp.apply_raise(10)
    assert emp.salary == 5500

def test_get_annual_salary():
    emp = Employee(2, "Bob", 4000)
    assert emp.get_annual_salary() == 48000

def test_raise_with_negative_percentage():
    emp = Employee(3, "Charlie", 3000)
    with pytest.raises(ValueError):
        emp.apply_raise(-5)
