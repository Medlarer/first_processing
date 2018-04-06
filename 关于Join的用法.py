from multiprocessing import Process
import time
import random
def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is piao end' %name)

p1=Process(target=piao,args=('egon',))
p2=Process(target=piao,args=('alex',))
p3=Process(target=piao,args=('yuanhao',))
p4=Process(target=piao,args=('wupeiqi',))

if __name__ == '__main__':

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print('主线程')
