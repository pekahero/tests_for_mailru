import math


#tuple
#test 1: is tuple constant.
def test_1():
    tpl = (1, 3, 6)
    try:
        tpl[1] = 5
    except TypeError:
        pass
    assert tpl[1] == 3


#test 2: can not delete tuple element
def test_2():
    tpl = (1, 3, 6)
    try:
        del tpl[1]
    except TypeError:
        pass
    assert len(tpl) == 3


#test 3: can delete tuple
def test_3():
    tpl = (1, 3, 6)
    del tpl
    try:
        assert print(tpl)
    except NameError:
        pass


#float
#test 4: is floor correct for negative float.
def even(x):
    return math.floor(x)


def test_4():
    assert even(-4.35) == -5


# test 5: int+float = float.
def int_plus_float(x, y):
    return x + y


def test_5():
    assert type(int_plus_float(5, 7.48)) == float


#test 6: int/float = float.
def int_div_by_float(x, y):
    return x/y


def test_6():
    assert type(int_div_by_float(3, 2.56)) == float

