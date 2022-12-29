import pytest
from employee import Employee


@pytest.fixture
def some_employee():
    some_employee = Employee('Juan', 'García', 12000)
    return some_employee


def test_give_default_raise(some_employee):    
    some_employee.give_raise()
    assert some_employee.annual_salary == 17000


def test_give_custom_raise(some_employee):
    some_employee.give_raise(8000)
    assert some_employee.annual_salary == 20000
    
    