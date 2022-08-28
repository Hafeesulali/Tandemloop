num = (input("Enter a number"))
if num == "x":
    i = 1
    while i > 0:
        if i % 2 != 0:
            print(i)
        i = i + 1

else:
    for i in range(1, int(num) * 2):
        if i % 2 != 0:
            print(i)
