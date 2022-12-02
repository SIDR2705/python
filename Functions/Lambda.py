
# Normal functions / Named functions
def Add(No1,No2):
    return  No1+No2

# Lambda functions / Unnamed functions
# lambda parameters : body

AddFunction= lambda A,B : A+B

Ans1=Add(10,11)
Ans2=AddFunction(10,11)

print("Additon using Normal function :",Ans1)
print("Additon using Lambda function :",Ans2)

print("Type of Lambda Function is : ",type(AddFunction))