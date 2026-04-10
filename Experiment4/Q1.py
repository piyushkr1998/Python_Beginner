'''s=str(input("Enter the string :"))
count=0
for i in s :
    if ('A'<=i<='Z') :
       count += 1
print("Number of capital letter ",count)'''

s=str(input("Enter the string :"))
count=0
for i in s:
    if i.isupper():
        count=count+1
print("Number of capital letter ",count)        