a=int(input("Enter the first number:"))
b=int(input("Enter second number :"))
c=int(input("Enter third number:"))

if (a > b and a > c):
    print("a is greater than b , c",a)

elif (b > a and b > c):
    print("b is greater than a , c",b)

else:
    print("c is greater than a , b",c)        