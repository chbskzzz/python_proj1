# CLASS DECORATORS
class x:
    def __init__(self):
        print("An instance of object was initialised")

    def __call__(self, *args, **kwargs):
        print("Arguments are ", args, kwargs)


a = x()
a = x()
print("calling objects or arguments")
a(4,5,z=12,v=20)
print("calling call function again")
a(8,9,r=30,t=40)

##
print("-"*40)
def y():
    print("doing something using function decorators")
    def z():
        print("naming " + x.__name__)
    return z


def repeatable():
    c = y()
    d = c()


repeatable()
##
print("-"*40)


class x1:
    def __init__(self):
        print("doing something using class decorator")

    def __call__(self):
        print("naming " + x.__name__)


def repeatable():
    c = x1()
    c()


repeatable()


