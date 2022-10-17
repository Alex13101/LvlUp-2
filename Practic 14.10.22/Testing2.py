import pytest

from utils import sort


def test_sort_z():
    lst=[2,3,4,5,6,]
    result = sort(lst)
    assert result == None

def test_sort_a():
    lst=[8,4,6,5,9,8]
    result = sort(lst)
    assert result == None

def test_sort_k():
    lst=[9,8,7,6,5,4,3]
    result = sort(lst)
    assert result == None



# def test_division_z():
#     a, b, = 30, 0
#
#     with pytest.raises(ZeroDivisionError):
#         division(a, b)

