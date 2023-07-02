'''
Types of EA Operators
__iadd__(self,other)        +=
__isub__(self,other)        -=
__imul__(self,other)        *=
__idiv__(self,other)        /=
__ifloordiv(self,other)     //=
__imod__(self,other)        %=
__ipow__(self,other)        **=
__ilshift__(self,other)     <<=
__irshift__(self,other)     >>=
__iand__(self,other)        &=
__ixor__(self,other)        ^=
__ior__(self,other)         |=
'''

class EAO:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return EAO(x,y)

    def __isub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return EAO(x,y)


obj1 = EAO(2,3)
print(obj1)
obj1 += EAO(3,5)
print(obj1)