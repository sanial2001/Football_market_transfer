
from typing import List
import random
from operator import mul
from functools import reduce

#   Problem 1

def splitword(word: str) -> List[str]:
    """Return the individual characters of the string.

    doctests:
    >>> splitword("doc")
    ['d', 'o', 'c']
    >>> splitword("abc")
    ['a', 'b', 'c']
    """
    return [char for char in word]

# Problem 2

def joinchar(char: List[str]) -> str: 
    """Returns a string after joining individual character.

    doctests:
    >>> joinchar(['d', 'o', 'c'])
    'doc'
    >>> joinchar (['a', 'b', 'c'])
    'abc'
    """
    word=''
    return word.join(char)

# Problem 3

def randomList(n: int) -> List[int]: 
    """Returns n random numbers.

    doctests:
    >>> randomList(1)
    [1]
    >>> randomList(0)
    []
    """
    numbers = random.sample(range(1, n + 1), n)
    return numbers

# Problem 4

def descendingSort(origList: List[int]) -> List[int]: 
    """Returns a sorted list in descending order.

    doctests:
    >>> descendingSort([3, 4, 1, 2, 5])
    [5, 4, 3, 2, 1]

    >>> descendingSort([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]

    """

    origList.sort(reverse=True)
    return origList

# Problem 5

def getFreq(numbers: List[int]) -> dict[int]: 
    """Returns the frequency of each number.

    doctests:
    >>> getFreq([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1: 2, 3: 3, 2: 4}
    >>> getFreq([1, 3, 2, 3, 1, 4, 2])
    {1: 2, 3: 2, 2: 2, 4: 1}

    """
    frequency = {}
    for i in range(len(numbers)):
        frequency.update({numbers[i]: numbers.count(numbers[i])})
    return frequency

# Problem 6

def uniqueElem(list1: List[int]) -> set(): 
    """Returns the unique element from the list.

    doctests:
    >>> uniqueElem([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> uniqueElem([1, 2, 5, 4, 3, 3, 2, 1, 4])
    {1, 2, 3, 4, 5}
    """
    list_set = set(list1)

    return list_set

# Problem 7

def repeatingElement(numbers: List[int]) -> set(): 
    """Returns the first element which repeats.

    doctests:
    >>> repeatingElement([1, 2, 3, 4, 5, 1, 2])
    1
    >>> repeatingElement([1, 3, 4, 2, 2, 4])
    2
    """
    repeatingnumber = set()
    for element in numbers:
        if element in repeatingnumber:
            return element
        elif element not in repeatingnumber:
            repeatingnumber.add(element)

    return repeatingnumber

# Problem 8

def squareAndCube(num: int) -> dict(): 
    """Returns a dictionary containing keys from 0 to n mapped with its square and cube.

    doctests:
    >>> squareAndCube(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> squareAndCube(2)
    {0: [0, 0], 1: [1, 1], 2: [4, 8]}
    """
    dictionary = {}
    for i in range(num + 1):
        value = [pow(i, 2), pow(i, 3)]
        dictionary.update({i: value})
    return dictionary

# Problem 9

def pairtuple(list1: list(), list2: list()) -> tuple():  
    """Returns tuples of each element of same index from two lists.

    >>> pairtuple([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
    >>> pairtuple([3, 2, 4], ['j', 'h', 'g'])
    ((3, 'j'), (2, 'h'), (4, 'g'))
    """
    ansTuple = zip(tuple(list1), tuple(list2))
    return tuple(ansTuple)

# Problem 10

def squaresUptoN(n: int) -> List[int]:  
    """Returns a list of squares from 0 to n.

    >>> squaresUptoN(5)
    [0, 1, 4, 9, 16, 25]
    >>> squaresUptoN(7)
    [0, 1, 4, 9, 16, 25, 36, 49]
    """
    squarelist = [pow(x, 2) for x in range(n + 1)]
    return squarelist

# Problem 11

def mappedSquare(n: int) -> List[int]:  
    """Returns a dictionary  mapping squares from 0 to n.
    >>> mappedSquare(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> mappedSquare(7)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
    """
    reqDict = {x: pow(x, 2) for x in range(n + 1)}
    return reqDict

# Problem 12

class MyClass:  
    """ class to apply the method 'apply' on a list of atomic values. 
    >>> a = MyClass([1, 2, 3, 4])
    >>> a.apply(lambda x: x*x)
    [1, 4, 9, 16]
    >>> a = MyClass([1, 2, 3, 4])
    >>> a.apply(lambda x: x - 1)
    [0, 1, 2, 3]
    """

    def __init__(self, variable):
        self.variable = variable

    def apply(self, func):
        try:
            return list(map(func, self.variable))
        except TypeError:
            raise Exception("error!") from TypeError()

# Problem 13

def transformToUppercase(originalList: List[str]) -> List[str]:  
    """Returns words that has been uppercased from an existing list wordList.

    >>> transformToUppercase(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    >>> transformToUppercase(['doc', 'now', 'run'])
    ['DOC', 'NOW', 'RUN']
    """
    reqlist = map(lambda x: x.upper(), originalList)
    return list(reqlist)

# Problem 14

def productOfNumbers(numbers: List[int]) -> int:  
    """Returns the product of all the given numbers.

    >>> productOfNumbers([1, 2, 3, 4, 5])
    120
    >>> productOfNumbers([5,6,2,8])
    480
    """
    answer = reduce(mul, numbers)
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
