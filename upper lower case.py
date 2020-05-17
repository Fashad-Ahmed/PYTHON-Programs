x = input("string;    ")
c = ""
for i in x:
    if ord(x)>64 and ord(x)<91:
        c+=x.lower()
    elif ord(x)>96 and ord(x)<123:
        c+=x.upper()
    else:
        c+=x
print(c)