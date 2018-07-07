import pytest
import re

from src.myQuery import my_query


def test_my_query1():
    regex = re.compile('Care|Quality|Commission')
    assert my_query(regex) == [0, 1, 2, 3, 4, 5, 6]


def test_my_query2():
    regex = re.compile('September|2004')
    assert my_query(regex) == [9]


def test_my_query3():
    regex = re.compile('general|population|generally')
    # regex2 = re.compile('September|2004')
    assert my_query(regex) == [6, 8]


def test_my_query4():
    regex = re.compile('Care Quality Commission|admission')
    # regex2 = re.compile('September|2004')
    assert my_query(regex) == [1]


def test_my_query5():
    regex = re.compile('general population|Alzheimer')
    assert my_query(regex) == [6]


def test_my_add():
    assert 1 + 1 == 2
