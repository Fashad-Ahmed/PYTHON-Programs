dict_1 = {0:"Zero",1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
dict_2={0:"",1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty", 9:"Ninty"}
dict_3={0:"",1:"Eleven",2:"Twelve",3:"Thirteen",4:"Fourteen",5:"Fifteen",6:"Sixteen",7:"Seventeen",8:"Eighteen",9:"Nineteen"}

num = input("enter a four digit number: ")
a=len(num)
if a==3:
    num = "0"+num
if a==2:
    num = "00"+num
if a==1:
    num = "000"+num

num1=int(num[0])
num2=int(num[1])
num3=int(num[2])
num4=int(num[3])

if(num1==num2==num3==num4==0):           #0000
    print("Zero")

if(num1==num2==num3==0 and num4!=0):                # 000?
    print(dict_1[num4])

if(num1==num2==0 and num3!=0):            # 00??
    if(num4==0):
      print(dict_2[num3])
    else:
        if(num3==1):
            print(dict_3[num4])
        else:
            print(dict_2[num3] + " " + dict_1[num4])

if(num1==0 and num2!=0):                            #0???
    if(num3==0):
        if(num4==0):
            print(dict_1[num2]+" Hundred")
        else:
            print(dict_1[num2] + " Hundred and " + dict_1[num4])
    else:
        if(num4==0):
            print(dict_1[num2] + " Hundred and " + dict_2[num3])
        else:
            if(num3==1):
                print(dict_1[num2] + " Hundred and " + dict_3[num4])
            else:
                print(dict_1[num2] + " Hundred and " + dict_2[num3]+" "+dict_1[num4])
if(num1!=0):
    if(num2==0):
        if(num3==0):
            if(num4==0):
                print(dict_1[num1]+" Thousand")
            else:
                print(dict_1[num1]+" Thousand and "+dict_1[num4])
        elif(num3==1):
            print(dict_1[num1]+" Thousand and "+dict_3[num4])
        else:
            if (num4 == 0):
                print(dict_1[num1] + " Thousand and "+dict_2[num3])
            else:
                print(dict_1[num1] + " Thousand and " + dict_2[num3] + " "+dict_1[num4])
    else:
        if (num3 == 0):
            if (num4 == 0):
                print(dict_1[num1] + " Thousand "+dict_1[num2]+" Hundred")
            else:
                print(dict_1[num1] + " Thousand "+dict_1[num2]+" Hundred and " + dict_1[num4])
        elif (num3 == 1):
            print(dict_1[num1] + " Thousand " + dict_1[num2] + " Hundred and " + dict_3[num4])
        else:
            if (num4 == 0):
                print(dict_1[num1] + " Thousand " + dict_1[num2] + " Hundred and " + dict_2[num3])
            else:
                print(dict_1[num1] + " Thousand " + dict_1[num2] + " Hundred and " + dict_2[num3]+" "+dict_1[num4])
