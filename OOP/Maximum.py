# Application to find out the Maximum Number

def Maximum(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    print("Enter first number :")
    Value1=int(input())

    print("Enter second number :")
    Value2=int(input())

    Ans=Maximum(Value1,Value2)

    print("Largest Number is : ",Ans)

if __name__=="__main__":
    main()