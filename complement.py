
c=""
a=0
for i in x:
    if a == 0 and i =="0":
        c+=i
    elif a == 0 and i == "1":
        c+=i
        a+=1
    else:
        if i=="1":
            c+="0"
        if i == '0':
            c+="1"
c=c[::-1]
print(c)