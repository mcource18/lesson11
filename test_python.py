import math

list_of_strings_1 = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
list_of_strings_2 = ['a', 'b', 'c']


def test_filter_isdigit_1():
    assert (list(filter(str.isdigit, list_of_strings_1)) == ['100', '1', '50'])


def test_filter_isdigit_2():
    assert (list(filter(str.isdigit, list_of_strings_2)) == [])


def test_map_len_1():
    assert (list(map(len, ('apple', 'banana', 'cherry'))) == [5, 6, 6])


def test_map_len_2():
    assert (list(map(len, ('max', 'kate', 'tom'))) == [3, 4, 3])


def test_sorted_1():
    assert (sorted([1,8,9,4]) == [1, 4, 8,9])

def test_sorted_2():
    assert (sorted(['max', 'kate', 'tom']) == ['kate','max','tom'])

# pi, sqrt, pow, hypot
def test_pi():
    assert (math.pi == 3.141592653589793)


def test_sqrt_1():
    assert (math.sqrt(9) == 3)


def test_sqrt_2():
    assert (math.sqrt(4) == 2)


def test_sqrt_3():
    assert (math.sqrt(16) == 4)


def test_pow_1():
    assert (math.pow(1, 3) == 1)


def test_pow_2():
    assert (math.pow(2, 3) == 8)


def test_pow_3():
    assert (math.pow(3, 3) == 27)


def test_hypot_1():
    assert (math.hypot(3, 4) == 5)
