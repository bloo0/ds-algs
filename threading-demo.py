import threading
import time

ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=count, args=(5,))
x.start() # main thread

x.join() # complete the operation of the thread


# 2nd thread
def count_2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

y = threading.Thread(target=count_2, args=(5,))
y.start() # main thread

y.join() # complete the operation of the thread


print(ls)
