from threading import Thread
import threading

class myThread(Thread):
    def run(self):
        print("Egyptian Pyramid")
        print(threading.current_thread().getName())
        for x in range(0,5):
            for j in range(0, x+1):
                print("*",end=" ")
            print("\r")

obj=myThread()
obj.start() # Thread-1
# obj.run() # MainThread