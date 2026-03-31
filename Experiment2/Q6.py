y=int(input("Enter any year"))

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :
    print("Year is leap year ",y)

else :
    print("Year is not leap year ")