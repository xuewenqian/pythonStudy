import threading,multiprocessing
def loop():
    x=0
    while True:
        x=x^1
        print(threading.current_thread().name)

for i in range(multiprocessing.cpu_count()):
    t=threading.Thread(target=loop)
    t.start()