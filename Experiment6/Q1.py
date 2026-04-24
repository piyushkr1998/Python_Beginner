def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum

nums = [10, 45, 2, 78, 34, 89, 5]
max_val, min_val = find_max_min(nums)

print("Maximum:", max_val)
print("Minimum:", min_val)