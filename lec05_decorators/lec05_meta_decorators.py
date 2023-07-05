# TYPES OF DECORATORS : 1) FUNCTION DECORATORS, 2) CLASS DECORATORS
def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function


def repeatable(b):
    x = outer_function("Hello ")
    d = x(b)
    print(d)


repeatable("bbb")
repeatable("ccc")

##

def join(function):
    function.data = 2
    return function


def add(x,y):
    return x+y+add.data


join(add)
c = add(5,4)
print(c)