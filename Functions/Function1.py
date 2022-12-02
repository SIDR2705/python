# Fuction which accepts nothing and returns nothing
def Demo1():
    print("Inside Demo1")

# Fuction which accepts one parameter and returns nothing
def Demo2(No):
    print("Inside Demo2 with argument :",No)

# Fuction which accepts one parameter and return one parameter
def Demo3(NO):
    print("Inside Demo2 with argument :",NO)
    return NO+2

# Fuction which accepts Two parameter and return One parameter
def Demo4(No1,No2):
    print("Inside Demo4")
    Add=No1+No2
    return Add

# Fuction which accepts Two parameter and return Two parameter
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub=No1-No2
    return Add,Sub

def main():
    Demo1()
    Demo2("Hello")
    Ans=Demo3(10)
    print("Return value of Demo3 is :",Ans)
    Ans= Demo4(10,11)
    print("Return value is :",Ans)
    Ans1,Ans2=Demo5(11,10)
    print("First reutn value: ",Ans1)
    print("Seconds reutn value: ", Ans2)


if __name__=="__main__":
    main()