lst = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst3 = []
count = {}
for i in lst2:
    for j in lst:
        if j % i == 0:
            lst3.append(i)
for k in lst3:
    if k not in count:
        count.update({k: 1})
    else:
        val = count[k]
        val = val + 1
        count.update({k: val})
print(count)
