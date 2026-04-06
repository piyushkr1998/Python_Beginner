num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    r = temp % 10
    sum = sum + r
    temp = temp // 10

print("Sum of digits =", sum)
