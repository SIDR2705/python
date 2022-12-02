print("Demonstration of Set")

# Data : Hetrogeneous
# Ordered : No
# Indexed : No
# Mutable : Yes
# Duplicates : No

data = {11,21,51,101,21,11}       # Duplicates
data1 = {11,90.80,True,"Hello"}  # Hetrogeneous

print("First set data : ",data)
print("Length of the data : ",len(data))
print("Data is Hetetogeneous : ",data1)
print("Data is Unordered : ",data1)
#print("Data is Index : ",data1[2])
print("Data is Unique elements : ",data)

print("Set is mutable")

# Insert element in set
data.add(211)
print("Data after insertion : ",data)

# Remove element in set
data.remove(211)
print("Data after removal : ",data)

data.discard(201)
print("Data after removal : ",data)





