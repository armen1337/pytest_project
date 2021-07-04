import pytest

from utils.employees import Employee


@pytest.fixture
def employee():
    return Employee("Alex", 25)


@pytest.fixture
def emp(employee):
    yield employee
    del employee

