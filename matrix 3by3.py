x=[]
for i in range(3):
    a=[]
    for j in range(3):
        b=int(input("value"))
        a.append(b)
    x.append(a)
print(x)
print("For determinant:")
print("Expanding by row1")
l=(x[0][0])*((x[1][1])*(x[2][2])-(x[1][2]*x[2][1]))
e=(x[0][1])*((x[1][0])*(x[2][2])-(x[1][2]*x[2][0]))
f=(x[0][2])*((x[1][0]*x[2][1])-(x[1][1]*x[2][0]))
d=l-e+f
print("D=",d)
if d==0:
    print("The matrix is singular")
else:
    print("For adjoint:")
    A = ((-1) ** (1 + 1)) * ((x[1][1] * x[2][2]) - (x[1][2] * x[2][1]))
    B = ((-1) ** (1 + 2)) * ((x[1][0] * x[2][2]) - (x[1][2] * x[2][0]))
    C = ((-1) ** (1 + 3)) * ((x[1][0] * x[2][1]) - (x[1][1] * x[2][0]))
    D = ((-1) ** (2 + 1)) * ((x[0][1] * x[2][2]) - (x[0][2] * x[2][1]))
    E = ((-1) ** (2 + 2)) * ((x[0][0] * x[2][2]) - (x[0][2] * x[2][0]))
    F = ((-1) ** (2 + 3)) * ((x[0][0] * x[2][1]) - (x[0][1] * x[2][0]))
    G = ((-1) ** (3 + 1)) * ((x[0][1] * x[1][2]) - (x[0][2] * x[1][1]))
    H = ((-1) ** (3 + 2)) * ((x[0][0] * x[1][2]) - (x[0][2] * x[1][0]))
    I = ((-1) ** (3 + 3)) * ((x[0][0] * x[1][1]) - (x[0][1] * x[1][0]))
    print([[A, D, G], [B, E, H], [C, F, I]])
    #if (A==1 and E==1 and I==1) and( B==C==D==F==G==H==0):
     #   print()
    print("[",A,"\t",B,"\t",C,"\n",D,"\t",E,"\t",F,"\n",G,"\t",H,"\t",I,"]")
    M = [A // d, D // d, G // d]
    N = [B // d, E // d, H // d]
    O = [C // d, F // d, I // d]
    print("The inverse is:")
    P = [M, N, O]
    print(P)


# x = int(input("#"))
# for i in range(x):
#     for j in range(x):
#         if ((i==j) or(i+j==x-1)) and (i<j):
#             print("*",end="")
#         else:
#             print("\t",end="")
#     print("\t")
