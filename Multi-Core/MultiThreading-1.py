import time
import threading

def DisplayEven(No):
    for i in range(1,No,1):
        if(i%2==0):
            print("Even Number :",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i%2 != 0):
            print("Odd Number :",i)

def main():
    print("Demonstartion of a Parallel Progamming using multiple Threads.")
    Number=2000

    p1=threading.Thread(target=DisplayEven,args=(Number,))
    p2=threading.Thread(target=DisplayOdd,args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__=="__main__":
    Start_time=time.process_time()
    main()
    End_time=time.process_time()
    print("Execution time is :",End_time-Start_time)
