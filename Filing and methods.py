# take each in list and made sub lists of each file and then break it up an datlast read it
file = open("office.txt","w")
x = int(input("ënter no. of records: "))
list2=[]
#list3=[]
#file = open("employee.txt","w")
for i in range(x):
    c = []
    list2.append(c)
    y = input("enter ur name: ")
    z = input("enter ur  id: ")
    a = input("enter your salary:")
    c.append(y)
    c.append(z)
    c.append(a)
   # list2.append([c])
# for k in range
print(list2)
for j in list2:
    x = ("\nEmployee Name: "+str(j[0]))
    ap = ("\n"+"User ID: "+str(j[1]))
    z = ("\n""Employee Salary: "+str(j[2]))
    #print(x,ap,z)
    file = open("office.txt","a")
    file.write(x+ap+z)
file = open("office.txt","r")
print(file.read())
file.close()
# import  os
# os.remove("office.txt")
