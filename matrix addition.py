c=int(input("rows:"))
d=int(input("columns: "))

mat=[]
mat2=[]

for a in range(c):
    max=[]
    for j in range(d):
        x = int(input("number: "))
        max.append(x)
    mat.append(max)


for b in range(c):
    min=[]
    for k in range(d):
        w=int(input("nomber:  "))
        min.append(w)
    mat2.append(min)

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(mat)):
   # iterate through columns
   for j in range(len(mat[0])):
       result[i][j] = mat[i][j] + mat2[i][j]

for r in result:
   print(r)

