from app.main import check_password
import pytest


def test_min_password_length():
    assert check_password("Pass@11") == False

def test_max_password_length():
    assert check_password("P@ssword123_P@ss1") == False

def test_contains_special_characters():
    assert check_password("Password1") == False

def test_password_contains_digits():
    assert check_password("P@ssword") == False

def test_password_contains_uppercase():
    assert check_password("p@ssword123_") == False