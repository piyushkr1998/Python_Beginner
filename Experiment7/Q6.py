filename = "counter.txt"

try:
   
    with open(filename, "r") as file:
        count = int(file.read())

except FileNotFoundError:
       count = 0

count += 1

with open(filename, "w") as file:
    file.write(str(count))
print("Program executed", count, "times")