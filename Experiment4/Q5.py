s = str(input("Enter the string"))
count = {}

for i in s:
    if i.isalpha():
        cap = i.upper()
    count[cap] = count.get(cap,0)+1
for key in count.keys():
    print(f"{count[key]}{key}")        