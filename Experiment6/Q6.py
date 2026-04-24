def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum
m_n=lambda list: find_max_min(nums)
nums = [10, 45, 2, 78, 34, 89, 5]
print(m_n(nums))
