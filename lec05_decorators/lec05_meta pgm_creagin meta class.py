# CREATING META CLASS
class x:
    pass


x.variable = 10

c = x()

# print(c.variable)

##

def metafunc():
    print("I am the metaclass function")


class inherit:
    def func(self,x,y):
        # print("I am the interited method")
        print(x+y)


metaobject = type('meta', (inherit,), dict(name="bbb", metafunction=metafunc))

# print(type(metaobject))   # <class 'type'>
b = metaobject()
# print(type(b))              # <class '__main__.meta'>

b.func(2,3)
print(b.name)