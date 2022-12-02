
def Add(No):
    if(No<=0):
        return 0
    else:
        Ans=Add(No-1)
        return (No+Ans)


def main():
    print("Enter the Number :")
    x=int(input())

    Ret=Add(x)
    print("The Result is : ",Ret)

if __name__=="__main__":
    main()