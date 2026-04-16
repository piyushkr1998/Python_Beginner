n=int(input("Enter the value of n :"))

count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0

for _ in range (n):

    x = int(input(""))

    if x==0 :
        count_0 = count_0 + 1
    elif x==1 :
        count_1 = count_1 + 1
    elif x==2:
        count_2 = count_2 + 1
    elif x==3:
        count_3 = count_3 + 1
print(count_0)
print(count_1)
print(count_2)
print(count_3)                   