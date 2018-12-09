from somepackage import add


def test_my_add():
    assert add.my_add([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
    assert add.my_add('beverly ', 'hills') == 'beverly hills'
