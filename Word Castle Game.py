print("************   WELCOME TO WORD GAME   **********")
print('1\t2\t3\t4\nA\tB\tC\tD\nE\tF\tG\tH\nI\tJ\tK\tL\nM\tN\tO\tP\nQ\tR\tS\tT\nU\tV\tW\tX\t\nY\tZ')
list_1=["A","E","I","M","Q","U","Y"]
list_2=["B","F","J","N","R","V","Z"]
list_3=["C","G","K","O","S","W"]
list_4=["D","H","L","P","T","X"]
x = int(input("Enter number of Characters of your guessed Word:"))
y=[] ; y2=[]
for i in range(1,x+1):
    y.append(int(input("Enter the Line Number: ")))
for j in y:
    if j == 1:
        y2.append(list_1)
        print(list_1)
    elif j == 2:
        y2.append(list_2)
        print(list_2)
    elif j == 3:
        y2.append(list_3)
        print(list_3)
    elif j == 4:
        y2.append(list_4)
        print(list_4)
horizontal_column=[]
for k in range(x):
    caulker=int(input("Enter the column numbers of your guessed word aplhabets: "))
    horizontal_column.append(caulker)
for j in range(len(horizontal_column)):
    f=y2[j][horizontal_column[j-1]]
    print(f,end="")
