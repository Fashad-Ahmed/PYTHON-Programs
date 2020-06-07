#   ******************* DIVISION METHOD ****************************
def check_armstong(x):
    k=0
    x1=str(x)
    kopiko=len(x1)
    x_a=x
    while x_a>0:
        x2=x_a%10
        k= k + x2**kopiko
        x_a=x_a//10
    if x==k:
        return "It is an Armstrong Number"
    else:
        return "It is not an Armstrong Number"
x=int(input("enter a number: "))
print(check_armstong(x))