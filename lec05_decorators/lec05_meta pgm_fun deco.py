def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function

z = outer_function(2)
v = outer_function(3)

print(z)
print(v)

ans1 = z(4)
ans2 = v(5)

print(ans1)
print(ans2)

def poly(a,b,c):
    def pol(x):
        return a*x**2 + b*x + c
    return pol

ans3 = poly(1,2,3)
w = ans3(4)
print(w)

# FUNCTION INSIDE FUNCTION, FUNCTION AS ARGUMENT, RETURN FUNCTION