# get(self, instance, owner)
# set(self, instance, value)
# delete(self, instance)

class cel:
    def __get__(self, instance, owner):
        return 5*(instance.x-32)/9

    def __set__(self, instance, value):
        instance.x=32+9*value/5


class Temp:
    y=cel()
    def __init__(self, x):
        self.x=x


t=Temp(112)
print(t.y)
t.y=0
print(t.x)