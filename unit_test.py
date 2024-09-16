from unittest import TestCase
from calculator import calc
from Palindroms import is_palin
import pytest

# class TryTesting(TestCase):
#     # def test_always_passes(self):
#     #     self.assertTrue(True)

#     # def test_always_fails(self):
#     #     self.assertTrue(False)
#     def test_uppercase(self):
#         assert "loud noises".upper() == "LOUD NOISES"
#     def test_reversed(self):
#         assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
#     def test_some_primes(self):
#         assert 37 in {
#             num
#             for num in range(2, 50)
#             if not any(num % div == 0 for div in range(2, num))
#         }  


def foo(arr, target):
    for a in range(0,len(arr)):
        for b in range(1, len(arr)):
            if arr[a] + arr[b] == target:
                strT = f'{a}:{b}'
                return strT
@pytest.mark.parametrize("test_input,target, expected", [([2 ,3, 5], 5, '0:1'), ([3 ,4, 2],5,'0:2')])
def test_index(test_input,target,expected):
    #assert foo([2, 5, 6,2],4) == '0:3'
    assert foo(test_input,target) == expected
def func(x):
    return x + 1
def test_answer():
    assert func(3) == 4
def test_cal():
    assert calc(2,3).total() == 5
@pytest.mark.parametrize("test_input,expected",[('kayak',True),('bob',True),('morning',False)])
def test_palin(test_input,expected):
    record_property("palidrom", 1
    assert is_palin(test_input) == expected
