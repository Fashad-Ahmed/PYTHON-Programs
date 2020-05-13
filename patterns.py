# ***************** effiel tower *********************
# x = int(input("#: "))
# for i in range(x):
#     for j in range(x):
#         if (j==x//2 ) or(i==j  and i>x//2) or (i+j==x-1 and i>x//2):
#              print("*\t",end="")
#         else:
#              print("\t",end="")
#     print("\t")

# ***************    right angle thera **********

# n = 10
# spaces=4
# for row in range(0,n):
#     for space in range(spaces):             #  right angle cone shape
#         print(" ",end="")
#     spaces+=1
#     for column in range(row):
#         print("* ",end="")
#     print()

# ************ Ulta pyramid *****************

# n = 10
# spaces=4
# for row in range(n,0,-1):          # ulta pyramid
#     for space in range(spaces):
#         print(" ",end="")
#     spaces+=1
#     for column in range(row):
#         print("* ",end="")
#     print()
#*****************************************************************************************************# x = int(input("enter the no. of rows: "))
#******************** diamond **************************************
# x = int(input("#:   "))
# for i in range(x):
#     print(" "*(x-i-1)+"* "*(i+1))
#
# for j in range(x-1,0,-1):
#     print(" "*(x-j)+"* "*(j))
# # ************ simple logic of pyramid ******************
# x = int(input("#: "))
# for i in range(x):
#     if i<=x//2:
#         for j in range(x//2-i):
#             print(" ",end="")
#         for k in range(i*2-1):
#             print("*",end="")
#     print()
#  **************************************************************

# ************************** diamond **************************
#
n = 9
print("Pattern 1")
# seedha pyramid

for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
    for a2 in range((n+1)//2 - a1):
        print(" ", end = "")
    for a3 in range((a1*2)-1):
        print("*", end = "")
    print()

# # ulta pyramid
#
# for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
#
#     for a2 in range(a1 - (n+1)//2):
#         print(" ", end = "")
#     for a3 in range((n+1 - a1)*2 - 1):
#         print("*", end = "")
#     print()
#************************************************************************************************
# x = int(input("string: "))
# for i in range(x):
#     for j in range(x):
#         if (i==x-1 or i==0) and j==x-1:
#             print("*",end="")
#        # elif ((i+j)%2 == 0 and i>j):
#     #    elif (i+j==x+1) and j>=i:
#      #       print("*",end="")
#         else:
#             print(" ",end="")
#     print().

# ******************* heart ********************************
# x= int(input("ënter: "))
# for row in range(x):
#     for col in range(x):
#         if row == 0 and col % 3 != 0 or row == 1 and col % 3 == 0 or row - col == 2 or row + col == 8:
#             print("*\t",end="")
#         else:
#             print("\t",end="")
#     print("\t")
#**************************************************************************************************************************
# for rows in range(15):
#     for col in range(15):
#         if (rows == 1 and col == 15 //2) or (rows == 0 and col != 15 // 2):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

#*********************** sir's ******************************

# x = int(input("#: "))
# for i in range(x):
#     for j in range(x):
#         if((i==j) or (i==0 or j==x-1) or (j==0 or i==x-1) or (i+j==x-1) or (j==x//2) or (i==x//2) ):
#              print("*\t",end="")
#         else:
#              print("\t",end="")
#     print("\t")
#****************************************
# x=9
# for i in range(x):
#     for j in range(x):
#         if (i==j) or (i+j==x-1 and j>i):
#             print("@\t",end="")
#         else:
#             print("\t",end="")
#     print("\t")