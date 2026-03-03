from user import User
import pytest


def test_valid_login():
    user = User("admin", "1234")
    assert user.login() == "Login successful"


def test_invalid_login():
    user = User("admin", "wrong")
    assert user.login() == "Login failed"


def test_empty_username():
    with pytest.raises(ValueError):
        User("", "1234")