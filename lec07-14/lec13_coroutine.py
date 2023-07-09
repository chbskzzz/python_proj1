def searching(string):
    print("Searching String: {}".format(string))
    while True:
        name = (yield)
        if string in name:
            print(name)


x = searching("ccc")
x.__next__()

x.send("bbb")
x.send("ccc")