import threading

Counter=0
lock=threading.Lock()

def Display():
    global Counter

    for i in range(100000):
        lock.acquire()
        Counter=Counter+1
        lock.release()

def main():

    t1=threading.Thread(target=Display)
    t2=threading.Thread(target=Display)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter:",Counter)

if __name__=="__main__":
    main()