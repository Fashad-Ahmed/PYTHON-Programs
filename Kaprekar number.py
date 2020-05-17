

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
