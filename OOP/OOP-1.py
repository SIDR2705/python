
class Arithmatic:

    def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addtion(self):
        Ans=self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans=self.No1- self.No2
        return Ans


def main ():
    print("Inside main method")

    obj = Arithmatic(11,10)

    Output=obj.Addtion()
    print("Addition is : ",Output)

    Output=obj.Subtraction()
    print("Subtraction is : ",Output)

if __name__=="__main__":
    print("Inside Starter ")
    main()