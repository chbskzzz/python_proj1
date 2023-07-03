'''
Types of Unary Operators
__neg__         -
__pos__         +
__abs__         abs
__invert__      ~
__complex__     cmp
__int__         int
__long__        long
__float__       float
__oct__         oct
__hex__         hex
'''

class x:
    def __init__(self,y):
        self.y = y

    def __neg__(self):
        return self.y

    def __pos__(self):
        return self.y

    def __invert__(self):
        return self.y

if __name__ == "__main__":
    obj1 = x(-2)
    # print(-obj1)
    # print(+obj1)
    print(~obj1)