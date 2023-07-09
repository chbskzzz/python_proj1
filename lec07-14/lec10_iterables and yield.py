import time

def call_received(received):
    a=0
    while True:
        if received=='yes':
            a=a+1
            return a
        else:
            return a

stoppage_time = time.time() + 5 * 60

while time.time() < stoppage_time:
    received = input('did you received a call')
    total = call_received(received)
    print(total)