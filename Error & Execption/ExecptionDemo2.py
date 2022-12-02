
def main():
    try:
        print("Enter First Number")
        No1=int(input())

        print("Enter Second Number")
        No2=int(input())


        Ans= No1/No2
        print("Division is : ",Ans)

    except ZeroDivisionError :
        print("Inside Zero Division Error")

    except ValueError:
        print("Inside Value Error")

    finally:
        print("\n Inside Finally Block")

if __name__=="__main__":
    main()