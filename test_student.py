import pytest
from student import *

def setup_function():
    students.clear()

def test_add_student():
    assert add_student(1, "Shruti") == True

def test_search_student():
    add_student(1, "Shruti")
    assert search_student(1) == "Shruti"

def test_remove_student():
    add_student(1, "Shruti")
    assert remove_student(1) == True

def test_remove_invalid():
    assert remove_student(2) == False

def test_update_student():
    add_student(1, "Shruti")
    assert update_student(1, "Priya") == True

def test_search_invalid():
    assert search_student(100) == None

def test_update_invalid():
    assert update_student(10, "ABC") == False

def test_multiple_students():
    add_student(1, "A")
    add_student(2, "B")
    assert search_student(2) == "B"

def test_duplicate_student():
    add_student(1, "A")
    add_student(1, "B")
    assert search_student(1) == "B"

def test_student_count():
    add_student(1, "A")
    add_student(2, "B")
    assert len(students) == 2