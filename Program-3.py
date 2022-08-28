num = (input("Enter a number"))
if num == "x":
    i = 1
    while i > 0:
        if i % 2 != 0:
            print(i)
        i = i + 1

else:
    a=int(num)
    if a%2==0:
        b=a-1
        for i in range(1,b*2):
            if i % 2 != 0:
                print(i)
    else:
        for i in range(1, a * 2):
            if i % 2 != 0:
                print(i)
