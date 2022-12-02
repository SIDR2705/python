# Swapping of Values
def Substraction(No1,No2):
    Ans=0
    Ans=No1-No2
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A<B):
            A,B=B,A
        return Function_Name(A,B)
    return Inner

def main():
    Value1=int(input("Enter First number : "))
    Value2 = int(input("Enter Second number : "))

    New_function= Decorated_Function(Substraction)
    Ret=(New_function(Value1,Value2))
    print("Substraction is :",Ret)

if __name__=="__main__":
    main()

