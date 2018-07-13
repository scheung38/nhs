import pytest
import re
import os

from src.part1_news_search import my_query, get_directory

os.chdir('..')


def test_my_query1():
    regex = re.compile('Care|Quality|Commission')
    assert my_query(regex, get_directory()) == [0, 1, 2, 3, 4, 5, 6]


def test_my_query2():
    regex = re.compile('September|2004')
    assert my_query(regex, get_directory()) == [9]


def test_my_query3():
    regex = re.compile('general|population|generally')
    # regex2 = re.compile('September|2004')
    assert my_query(regex, get_directory()) == [6, 8]


def test_my_query4():
    regex = re.compile('Care Quality Commission|admission')
    # regex2 = re.compile('September|2004')
    assert my_query(regex, get_directory()) == [1]


def test_my_query5():
    regex = re.compile('general population|Alzheimer')
    assert my_query(regex, get_directory()) == [6]


def test_my_add():
    assert 1 + 1 == 2
