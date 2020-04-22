# Dec to Bin
dec = int(input("Enter Decimal Number: "))
binary = ''
while dec > 0:
    if dec % 2 == 1:
        binary = '1' + binary
    else:
        binary = '0' + binary
    dec = dec // 2
print(binary)
while len(binary) % 4 != 0:
    binary = '0' + binary
binary = binary[::-1]
bin2 = ''
hexa = ''
i = 0
while i < len(binary):
    var = 0
    bin2 = bin2 + binary[i]
    if len(bin2) % 4 == 0:
        var += int(bin2[0])*1
        var += int(bin2[1])*2
        var += int(bin2[2])*4
        var += int(bin2[3])*8
        if var < 10:
            hexa += str(var)
        else:
            if var == 10:
                hexa += 'A'
            elif var == 11:
                hexa += 'B'
            elif var == 12:
                hexa += 'C'
            elif var == 13:
                hexa += 'D'
            elif var == 14:
                hexa += 'E'
            elif var == 15:
                hexa += 'F'
        bin2 = ''
    i +=1
hexa = hexa[::-1]
print(hexa)