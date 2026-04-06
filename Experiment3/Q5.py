n=int(input("Enter the value of n :"))
rev=0
temp=n

while temp>0:
   r = temp%10
   rev = rev *10 +r
   temp = temp //10

if n==rev:
    print("Number is palindrom ",n)
else:
    print("Number is not palindrom number ",n)        