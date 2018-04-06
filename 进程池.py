from multiprocessing import Pool
import os,time
def work(n):
    print("%s run" %os.getpid())
    time.sleep(1)
    return n**2

if __name__ == '__main__':
    p = Pool(3) #从进程池中从无到有创建三个进程，以后一直是这三个执行任务
    res_l = []
    for i in range(10):
        res = p.apply_async(work,args=(i,)) #同步运行，阻塞，直到本次任务执行完毕
        res_l.append(res)
    #异步apply_async的用法，如果使用异步提交的任务，主进程需要使用join，等待进程池内任务处理完，再用get
        # 收集结果，否则，主进程结束，进程池还未结束，也跟着结束了
    p.close()
    p.join()
    for res in res_l:
        print(res.get()) #使用get获取apply_aync的结果，,如果是apply,则没有get方法,因为apply是同步执行,
            # 立刻获取结果,也根本无需get
