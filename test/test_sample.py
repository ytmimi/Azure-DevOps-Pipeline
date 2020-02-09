from sample_package.sample import add, sub


def test_add():
    assert add(7, 8) == 15


def test_sub():
    assert sub(-1, -5) == 4
