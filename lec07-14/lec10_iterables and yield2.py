import time

def x():
    yield 'a'
    yield 'b'
    yield 'c'

y = x()
for i in range(3):
    print(y.__next__())


def calls_received(received):
    a = 0
    while True:
        if received == 'yes':
            a=a+1
            received = yield a
        else:
            received = yield a


# rec = calls_received()
# rec.__next__()

stoppage_time = time.time() + 5 * 60
while time.time() < stoppage_time:
    ans = input('do you received a call or not')
    print(str(rec.send(ans)))