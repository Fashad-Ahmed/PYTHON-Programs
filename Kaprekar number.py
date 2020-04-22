# x=input("enter a number: ")
# a=int(x)**2
# print("square: ",a)
# a1=str(a)
# x1=a1[0:2]
# x2=a1[2:]
#
# x1=int(x1)
# x2=int(x2)
#
# print(x1);print(x2)
# #
# if x1+x2 == int(x):
#     print("kaprekar")
# else:
#     print("kaprekar")
def kek():
    a=int(input("Number: "))
    b=str(a*a)
    f="It is a Kaprekar number"
    if len(str(b))>1:
        if len(str(b))%2==0:
            c=int(len(str(b))/2)
            print(b)
            e=int(b[:c])+int(b[c:])
            print(e)
            if e==a:
                f="It is a Kaprekar number!"
            else:
                f="It is not Kaprekar number"
        elif len(str(b))%2==1:
            c = int((len(str(b))/2))+1
            print(b)
            e = int(b[:c-1]) + int(b[c-1:])
            g= int(b[:c]) + int(b[c+1:])
            print(g)
            print(e)
            if e==a or g==a:
                f="It is a Kaprekar number"
            else:
                f="It is not Kaprekar number"
        print(f)
    elif len(str(b))==1:
        print(f)
kek()