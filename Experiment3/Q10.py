n = 5

for i in range(n):

    for j in range(1, n - i + 1):
        print(j, end="")

    if i == 0:
        for j in range(n - 1, 0, -1):
            print(j, end="")
    else:
        print(" " * i, end="")
        for k in range(i):
            print("* ", end="")
        print(" " * (i - 1), end="")

        for j in range(n - i, 0, -1):
            print(j, end="")

    print()
