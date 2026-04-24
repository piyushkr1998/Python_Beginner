n=int(input("Enter the value of n :"))

list = []
for _ in range (n):
     list.append(float(input()))

t = tuple(list)
avg = sum(t)/len(t)

print("The created tuple is :",t)
print("The the average of tuple is :",avg)