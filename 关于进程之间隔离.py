from multiprocessing import Process

n = 100 #在windows系统中把全局变量定义在 __name__ == "__main__"
def work():
    global n
    n = 0
    print("子进程内：",n)

if __name__ == '__main__':
    p = Process(target=work)
    p.start()