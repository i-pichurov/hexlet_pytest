from reverse import reverse_func


def test_reverse():
    with open('/home/ilya/hexlet_pytest/tests/fixtures/before.txt') as f:
        before = f.read()
    with open ('/home/ilya/hexlet_pytest/tests/fixtures/result.txt') as r:
        result = r.read()
    before_reversed = reverse_func(before)
    assert before_reversed == result
