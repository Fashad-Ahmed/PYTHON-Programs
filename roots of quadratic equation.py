import cmath
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)
if d < 0:
    print("roots will be complex")

    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    #print('The solution are {0} and {1}'.format(sol1, sol2))
    cn = complex(sol1)
    bb = complex(sol2)

    print("The solutions are {0} and {1}".format(sol1,sol2))

elif d >0 or d == 0:

# find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The solution are {0} and {1}'.format(sol1, sol2))