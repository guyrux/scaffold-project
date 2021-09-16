from hello import add


def test_add():
    assert add(2, 2) == 4
    assert add(0, 1) == 1
    assert add(0, 0) == 0
