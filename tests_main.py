from main import(
    factorial,
    prime,
    element,
    sort
)

def test_factorials():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(2) == 4
    assert factorial(-1) == None
    assert factorial(8) == 40380
    assert factorial(10) == 3628800
    assert factorial(-5) == None
    assert factorial(4) == 24
    assert factorial(11) == 39916800
    assert factorial(7) == 5040


def test_primes():
    assert prime(2) == True
    assert prime(7) == True
    assert prime(15) == False
    assert prime(6) == False
    assert prime(3) == True
    assert prime(1) == False
    assert prime(0) == False
    assert prime(11) == True
    assert prime(12) == False
    assert prime(5) == True


def test_elements():
    assert element([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert element([1, 1, 1, 1, 1]) == [1]
    assert element([10, 5, 0, -2, 3, 5, 10, 1, 0]) == [10, 5, 0, -2, 3, 1]
    assert element([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert element([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert element([0, 0, 0, 1, 1, 2]) == [0, 1, 2]
    assert element([10, 20, 30, 10, 20, 40]) == [10, 20, 30, 40]
    assert element(['a', 'a', 'b', 'b', 'c']) == ['a', 'b', 'c']
    assert element([True, True, False, True]) == [True, False]
    assert element([None, None, 1, 2, None]) == [None, 1, 2]

def test_sorts():
    
    assert sort(words=["cat"]) == {3: ["cat"]}
    assert sort(words=["cat", "dog", "elephant"]) == {3: ["cat", "dog"], 8: ["elephant"]}
    assert sort(words=[]) == {}
    assert sort(words=["bat", "cat", "rat"]) == {3: ["bat", "cat", "rat"]}
    assert sort(words=["apple", "bat", "cat", "banana", "dog"]) == {5: ["apple"], 3: ["bat", "cat", "dog"], 6: ["banana"]}
    assert sort(words=["a", "be", "cat", "dog", "elephant"]) == {1: ["a"], 2: ["be"], 3: ["cat", "dog"], 8: ["elephant"]}
    assert sort(words=["Cat", "dog", "DOG"]) == {3: ["Cat", "dog", "DOG"]}
    assert sort(words=["a ", " be", "cat ", " dog", "elephant "]) == {2: ["a "], 3: [" be", " dog"], 4: ["cat "], 9: ["elephant "]}
    assert sort(words=["", "a", "ab", "abc"]) == {0: [""], 1: ["a"], 2: ["ab"], 3: ["abc"]}
    assert sort(words=["cat", "bat", "rat", "hat!"]) == {3: ["cat", "bat", "rat"], 4: ["hat!"]}

