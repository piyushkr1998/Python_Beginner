list1 = ["a", "b", "c", "d"]
list2 = [10, 20, 30, 40]

result_dict = {}

for i in range(len(list1)):
    result_dict[list1[i]] = list2[i]

print("Generated Dictionary:", result_dict)