
def test_1():
    x = 10
    y = 10
    assert x == y


def test_2():
    name = "madam"
    assert name == name[::-1], "Not a palindrome"


def test_3():
    word = "selenium"
    title = "selenium is used for automation"
    assert word in title, "title does not contain selenium word"


def test_4():
    word = "selenium"
    title = "selenium is used for automation"
    assert word is title, "title does not contain selenium word"
