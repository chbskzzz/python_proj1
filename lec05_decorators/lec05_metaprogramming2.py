def addition(a,b):
    def add(x,y):
        return x+y

    sum = "the sum of two no,s is " + str(add(a,b))
    return sum

Answer = addition(2,3)
print(Answer)