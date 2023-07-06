class cel:
    def __init__(self, value=0.0):
        self.value=float(value)
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)

class feh:
    def __get__(self,instance,owner):
        return instance.cel * 9/5 + 32
    def __set__(self,instance,value):
        instance.cel=(float(value)-32) *5/9

class temp:
    cel=cel(112)
    feh=feh()
    print(cel.value)

t = temp()
print(t.feh)