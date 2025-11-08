"""
Tests for the class Calculator. We test four arithmetic operations and potential errors.
"""

import pytest

from calculator import Calculator

def test_answer1():
    calculator = Calculator(2, 3)
    assert calculator.sum() == 5

def test_answer1e():
    calculator = Calculator("s", 3)
    assert calculator.sum() == None

def test_answer2():
    calculator = Calculator(2, 3)
    assert calculator.subtract() == -1

def test_answer2e():
    calculator = Calculator("t", "s")
    assert calculator.subtract() == None

def test_answer3():
    calculator = Calculator(2, 3)
    assert calculator.multiply() == 6

def test_answer3e():
    calculator = Calculator("j", "j")
    assert calculator.multiply() == None

def test_answer4():
    calculator = Calculator(5, 5)
    assert calculator.divide() == 1

def test_answer4e1():
    calculator = Calculator("dsd", 5)
    assert calculator.divide() == None

def test_answer4e2():
    calculator = Calculator(5, 0)
    assert calculator.divide() == None