try:
    with open("numbers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]

    if numbers:
        max_num = max(numbers)
    else:
        max_num = "No numbers found"
    if numbers:
        avg = sum(numbers) / len(numbers)
    else:
        avg = 0
    count_gt_100 = sum(1 for num in numbers if num > 100)

    print("Maximum number:", max_num)
    print("Average:", avg)
    print("Numbers greater than 100:", count_gt_100)

except FileNotFoundError:
    print("File not found! Please check the file location.")
except ValueError:
    print("File contains non-integer values!")