# Data : Hetrogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicates : Yes

Data = [11,21,51,101]

print("Output using for")
for no in Data:
    print(no,end=" ")
print("\n-----------------------------------")

print("Output using for with Index")
for i in range(0,len(Data)):
    print(Data[i],end=" ")
print("\n-----------------------------------")

print("Output using While with Index")
i=0
while(i<len(Data)):
    print(Data[i],end=" ")
    i+=1        # i = i+1
print("\n-----------------------------------")