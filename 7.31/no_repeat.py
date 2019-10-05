list1 = [0, 2, 3, 4, 5, 5, 6, 1]
temp1 = list(set(list1))
print(temp1)
###this will change the order



list2 = [0, 2, 3, 4, 5, 5, 6, 1]
temp2 = []
for each in list2:
    if each not in temp2:
        temp2.append(each)
print(temp2)
###to keep the original order
