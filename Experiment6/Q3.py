n=int(input("Enter he value of n :"))
list_score=[]
for _ in range (n):
    list_score.append(int(input()))
    x = list(set (list_score))
    x.sort()

runnerup = x[-2]

print("The runnerup is :",runnerup)