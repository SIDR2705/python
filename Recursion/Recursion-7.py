
def Display(No):
    Ans=0
    while(No>=0):

        Ans=Ans+No
        No = No - 1

    return Ans


def main():
    print("Enter the Number :")
    x=int(input())

    Ret=Display(x)
    print("The Result is : ",Ret)

if __name__=="__main__":
    main()