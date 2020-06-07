x=[]
y=[]
length = int(input("Enter the length of lists: "))
for i in range(length):
    a = int(input("Enter the members of list: "))
    x.append(a)
for j in range(length):
    b = int(input("Enter the memebrs of list: "))
    y.append(b)
print("***  BEFORE SWAP ***")
print(x) ; print(y)
for k in range(length):
    x[k] = x[k] + y[k]
    y[k] = x[k] - y[k]
    x[k] = x[k] - y[k]
print("***  AFTER SWAP  ***")
print(x) ; print(y)