print("Demonstration of list")

# Data : Hetrogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicates : Yes

data = [11,21,51,101,21,11]         # Duplicates
data1 = [11,90.80,True,"Hello"]  # Hetrogeneous

print("Data is Hetetogeneous : ",data1)
print("Data is Ordered : ",data1)
print("Data is Index : ",data1[2])
print("Data is duplicate elements : ",data)

print("List is mutable")
data.append(201)
print("Data after append : ",data)
data.pop()
print("Data after pop : ",data)



