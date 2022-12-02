Batches = {"PPA":18000,"LB":16700,"Python": 16500,"Angular":15000}

print("Data of Dictionary : ",Batches)

print("\n------------------------------------")

print("Data traversal using for-loop")
for x in Batches:
    print(x)
print("\n------------------------------------")

print("Data traversal using for-loop")
for x in Batches:
    print(x,Batches[x])
print("\n------------------------------------")

print("Data traversal using for-loop")
for x in Batches:
    print(x,Batches.get(x))
print("\n------------------------------------")

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)
print("\n------------------------------------")

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)
print("\n------------------------------------")

