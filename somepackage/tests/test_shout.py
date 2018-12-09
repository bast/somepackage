from somepackage import shout


def test_shout_and_repeat():
    result = shout.shout_and_repeat('hello goodbye-')
    assert result == 'HELLO GOODBYE-HELLO GOODBYE-'


def test_shout():
    assert shout._shout('have a nice day') == 'HAVE A NICE DAY'
