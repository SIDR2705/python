# Taking input fom the user and inserting into the list
def main():
    List= list()

    print("Enter how many elements you want to store ?")
    size=int(input())

    print("Please enter the values :")

    for i in range(0,size,1):
        no=int(input())
        List.append(no)    #List.insert(i,no)

    print(List)

if __name__=="__main__":
    main()