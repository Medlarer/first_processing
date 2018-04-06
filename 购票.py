from multiprocessing import Process,Lock
import time,json,random

def search():
    dic = json.load(open("db"))
    print("\033[43m剩余票数%s\033[0m" %dic["count"])

def get():
    dic = json.load(open("db"))
    time.sleep(0.1)
    if dic["count"] > 0:
        dic["count"] -= 1
        time.sleep(0.2)
        json.dump(dic,open("db","w"))
        print('\033[43m购票成功\033[0m')

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(100):
        p = Process(target=task,args=(lock,))
        p.start()