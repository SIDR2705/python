
def Factorial(No):
    if(No<=0):
        return 1
    else:
        Ans=Factorial(No-1)
        return (No*Ans)


def main():
    print("Enter the Number :")
    x=int(input())

    Ret=Factorial(x)
    print("The Result is :",Ret)

if __name__=="__main__":
    main()