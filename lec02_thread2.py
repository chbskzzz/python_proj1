from threading import Thread
import threading

def even_odd():
    evenNo()
    # print(threading.current_thread().getName())
    oddNo()

def evenNo():
    print("Even No are\n")
    for x in range(10):
        if (x%2 == 0):
            print(x)
    print(threading.current_thread().getName())

def oddNo():
    print("Odd No are\n")
    for x in range(10):
        if (x%2 != 0):
            print(x)

t = Thread(target=even_odd, name="Even_Odd Thread")
t.start()