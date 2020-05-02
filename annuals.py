# f = [10,19,5,1,7,14,0,7,5]
# c=0
# for i in f:
#     print(c," ",i," ", i  * "*")
#     c+=1

# pattern

x = 5
for i in range(x):
    var = i + 1
    c = x - 1
    for j in range(i+1):
        print(format(var,'<4'),end='')
        var = var + c
        c = c - 1
    print( )
    #print(var)
