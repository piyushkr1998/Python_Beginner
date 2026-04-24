def soc(n):
    total=0
    i=0
    while i < n:
        total = total + i*i*i
        i=i+1
    return total
sum = soc(5)

print(sum)