import pytest

from utils.employees import Employee


##### Positive test cases  #####

@pytest.mark.positive
def test_name_and_age(emp):
    assert emp.name == "Alex" and emp.age == 25


@pytest.mark.positive
def test_add_employee_and_get_count(emp):
    emp2 = Employee("Melissa", 22)
    assert Employee.count == 2


@pytest.mark.positive
def test_employee_status_is_currently_working(emp):
    assert emp.status == "Currently working"


@pytest.mark.positive
def test_employee_status_becomes_fired_after_firing(emp):
    emp.fire()
    assert emp.status == "Fired"


##### Negative test cases  #####

@pytest.mark.negative
def test_verify_error_message_on_changing_status(emp):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        emp.status = "Boss"


@pytest.mark.negative
def test_verify_error_message_on_changing_name(emp):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        emp.name = "Anthony"


@pytest.mark.negative
def test_verify_error_message_on_changing_age(emp):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        emp.name = 33




