list1 = []
a = int(input("enter range: "))
for x in range(a):
    b =int(input("enter number: "))
    list1.append(b)
for y in range(a):
    for z in range(y+1,a):
        if list1[y] > list1[z]:
            asc = list1[y]
            list1[y] = list1[z]
            list1[z] = asc
print(list1)


print("in desceding order")

print(list1[::-1])
