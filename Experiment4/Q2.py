s=str(input("Enter the string:"))
Vowels = 'AEIOUaeiou'
count = 0
for i in s:
    if i in Vowels:
        count=count+1
print("Number of vowels in string :",count)