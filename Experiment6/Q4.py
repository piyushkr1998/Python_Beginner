# Input number of persons
n = int(input("Enter number of persons: "))

# Create dictionary
students = {}

# Taking input
for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

# a) Display all names
print("\nAll Names:")
for name in students.keys():
    print(name)

# b) Display all cities
print("\nAll Cities:")
for city in students.values():
    print(city)

# c) Display student name and city
print("\nStudent Name and City:")
for name, city in students.items():
    print(name, "->", city)

# d) Count number of students in each city
city_count = {}

for city in students.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nNumber of students in each city:")
for city, count in city_count.items():
    print(city, ":", count)