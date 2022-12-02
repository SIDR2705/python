
def Area(Radius,PI=3.14):
    Result = PI*Radius*Radius
    return Result

def main():
    RValue= 10.5
    PIValue=3.14

    # Postional argumments
    Ans=Area(RValue,PIValue)
    print("Area of the circle is :",Ans)

    # Keyword argumments
    Ans=Area(PI=PIValue,Radius=RValue)
    print("Area of the circle is :",Ans)

    # Postional argumment and second is Default
    Ans = Area(10.5)
    print("Area of the circle is :", Ans)

    # Keyword argumment and second is Default
    Ans=Area(Radius=10.5)
    print("Area of the circle is :",Ans)

    # Keyword argumments
    Ans=Area(PI=7.10,Radius=10.5)
    print("Area of the circle is :",Ans)



if __name__=="__main__":
    main()