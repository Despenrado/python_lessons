import pytest

def union(*args):
    newSet = set()
    
    for elem in args:
        newSet.update(elem)
        
    return newSet

@pytest.mark.parametrize("setList, expected",[
    (({1,2,3},{1,2,3},{3,4,5}), {1,2,3,4,5}),
    (({"a", "b", 1}, {2,"4"}), {"a","b", 1, 2, "4"})
])
def test_union(setList : tuple, expected : set):
    assert union(*setList) == expected
    
    
    
EXCEPTION_IS_NEGATIVE = Exception("Variable should be gather or equals 0")

def digits(n : int):
    if n < 0 :
        raise EXCEPTION_IS_NEGATIVE
    
    if n == 0:
        return [0]
    
    res = []
    base = 10
    while n > 0:
        res.append(n % base)
        n = n // base
        
    return res[::-1]


@pytest.mark.parametrize("n, expected",[
    (0, [0]),
    (123, [1,2,3]),
    (1914, [1,9,1,4])
])
def test_digitst(n : int, expected : int):
    assert digits(n) == expected
    
    
@pytest.mark.parametrize("n",[
    (-1),
])
def test_digitst_exception(n : int):
    with pytest.raises(Exception):
        digits(n)
        
        
        
def gcd(a, b):
    while b:
        a,b = b, a % b
    return a

@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 2),
    (12, 6, 6)
])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected
    

def _lcm(a, b):
    return abs(a*b) // gcd(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 12),
    (7, 6, 42)
])
def test__lcm(a, b, expected):
    assert _lcm(a, b) == expected

def lcm(*args):
    if not args:
        return 0
    
    currLCM = args[0]
    for num in args[1:]:
        currLCM = _lcm(currLCM, num)
    return currLCM

@pytest.mark.parametrize("a, expected", [
    ((4, 6, 10), 60),
    ((7, 6, 81), 1134),
    ((100500, 42), 703500),
    ((range(2, 40, 8)), 19890),
])
def test_lcm(a, expected):
    assert lcm(*a) == expected
    

from functools import reduce


def compose(*functions):
    def compose_two(f, g):
        return lambda x: f(g(x))
    
    return reduce(compose_two, functions)
    
    
def test_compose():
    f = compose(lambda x: 2 * x, lambda x: x + 1, lambda x: x % 9)
    assert f(42) == 14
