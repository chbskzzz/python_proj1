# Types of Magic Methods:
# 1. Binary Operators
# 2. Unary Operators
# 3. Comparison Operators
# 4. Extended Assignment
'''
Types of Binary Operators
__add__(self, other)            +, add
__sub__(self, other)            -, sub
__mul__(self, other)            *, mul
__div__(self, other)            /, div
__floordiv__(self, other)       //, floor
__mod__(self, other)            %, mod
__pow__(self, other)            **, power
__lshift__(self, other)         <<, left shift
__rshift__(self, other)         >>, right shift
__and__(self, other)            &, and
__xor__(self, other)            ^, xor
__or__(self, other)             |, or

'''



class Addition:
    def __init__(self, *arguments):
        if len(arguments) == 0:
            self.numbers = (0,0)
        else:
            self.numbers = arguments

    def __add__(self, other):
        sum = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        return Addition(*sum)

    def __mul__(self, other):
        mul = tuple(x * y for x, y in zip(self.numbers, other.numbers))
        return Addition(*mul)

    def __sub__(self, other):
        sub = tuple(x - y for x, y in zip(self.numbers, other.numbers))
        return Addition(*sub)


obj1 = Addition(2,3,)
obj2 = Addition(4,5,)
obj3 = obj1 + obj2
obj4 = obj1 * obj2
obj5 = obj1 - obj2
print(obj3.numbers)
print(obj4.numbers)
print(obj5.numbers)