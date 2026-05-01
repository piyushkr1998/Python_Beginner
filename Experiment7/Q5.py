try:
    with open("data.txt", "r") as file:
        data = file.readlines()

    numbers = [int(line.strip()) for line in data if line.strip()]

    if not numbers:
        raise ValueError("File is empty")
    print("Maximum number:", max(numbers))

except FileNotFoundError:
    print("Error: File not found")
except ValueError as e:
    print("Error:", e)

except PermissionError:
    print("Error: Permission denied")

except Exception as e:
    print("Unexpected Error:", e)