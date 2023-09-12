import pytest
import sys


@pytest.mark.parametrize("username,password",
                         [
                             ('david', 'password1'),
                             ('james', 'password2'),
                             ('smith', 'password3')
                         ]
                         )


def test_login(username,password):
    print(username)
    print(password)


