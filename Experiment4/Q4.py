string=input("Enter the string :")
sub=input("Enter second string ")
count=0
start=0
while True:
    pos = string.find(sub,start)
    if pos==-1:
        break
    count = count + 1
    start = pos + 1
print(count)    