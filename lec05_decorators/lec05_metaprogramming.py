# META PROGRAMMING : Decorators, Class Decorators, Meta Classes
# Type of Decorators. 1) Function Decorators, Class Decorators

def outside_Function():
    def inside_Function():
        print("Hey, I am the inside Function")
        # outside_Function()

    print("Hey, I am the outside Function")
    inside_Function()

outside_Function()