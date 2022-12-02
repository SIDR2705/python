# Accepts 2 numbers and perform addition and subtraction of It

# Kay karych ahe ??       -> Behaviours (Function)
# -- Addition and Subtraction

# Te karyla Kai lagtanar ahe??       -> Characteristics(Data)
# -- Input of numbers

# Class = Characteristics + Behaviours
# Class = Data + Functions


class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def Add(self):
        return self.No1+self.No2

    def Sub(self):
        return self.No1-self.No2


def main():
    print("Enter first number")
    Value1=int(input())

    print("Enter second number")
    Value2=int(input())

    obj= Arithematic(Value1,Value2)

    Ans=obj.Add()
    print("Addtion is : ",Ans)

    Ans=obj.Sub()
    print("Subtraction is : ",Ans)

if __name__=="__main__":
    main()