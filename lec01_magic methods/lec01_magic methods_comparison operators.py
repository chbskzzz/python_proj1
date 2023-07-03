'''
Types of Comparison
obj.__lt__          <
obj.__gt__          >
obj.__eq__          ==
obj.__ge__          >=
obj.__le__          <=
obj.__ne__          !=
'''

class comparison:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x


if __name__ == '__main__':
    obj1 = comparison(2)
    obj2 = comparison(4)
    print(obj1<obj2)
    print(obj1>obj2)
    print(obj1==obj2)