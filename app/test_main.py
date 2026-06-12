from app.main import check_password


def test_min_password_length() -> None:
    assert check_password("Pass@11") == False


def test_max_password_length() -> None:
    assert check_password("P@ssword123_P@ss1") == False


def test_contains_special_characters() -> None:
    assert check_password("Password1") == False


def test_password_contains_digits() -> None:
    assert check_password("P@ssword") == False


def test_password_contains_uppercase() -> None:
    assert check_password("p@ssword123_") == False
