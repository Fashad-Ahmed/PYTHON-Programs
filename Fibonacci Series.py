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

#
# list=[]
# x=int(input(": "))
# for i in range(x):
#     b=int(input(": "))
#     list.append(b)
# for j in range(a):
#     for k in range(j+1,a):
#         if list[j]>list[k]:
#             abc = list[j]
#             list[j] = list[k]
#             list[j] = abc
# print(list)