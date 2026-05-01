try:
    with open("name.txt", "r") as file:
        names = file.readlines()

    names = [name.strip() for name in names if name.strip()]

    total_names = len(names)

    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_count = sum(1 for name in names if name.lower().startswith(vowels))

    if names:
        longest_name = max(names, key=len)
    else:
        longest_name = "No names found"

    print("Total names:", total_names)
    print("Names starting with vowel:", vowel_count)
    print("Longest name:", longest_name)

except FileNotFoundError:
    print("File not found! Please check the file location.")