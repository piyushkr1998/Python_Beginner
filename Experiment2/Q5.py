a=int(input("Enter first value : "))
b=int(input("Enter second value :"))
c=int(input("Enter third value :"))
 
D = b*b - 4*a*c

if D > 0:
    print("Roots are real and disticnt ")
    r1 = (-b + D**0.5) / (2*a)
    r2 = (-b - D**0.5) / (2*a)
    print("Root 1 =",r1)
    print("Root 2 =",r2)

elif D == 0:
    print("Roots are real and equal ")
    r = -b / (2*a)
    print("Root is =",r)

else:
    print("Roots are imaginary")

