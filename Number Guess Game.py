import time

print("                                        **********\nWelcome to a GAME OF SUM. In this what I gonna do is to surprise you by my trick. Simply this game contains 5 steps,\nin which  three turns is yours while the remaining lefts are mine!Firstly, You have to enter a double digit number \nand just after doing the sum interpreter will tell you the sum of upcoming four numbers which you & me gonna have to \nenter. Then, in second turn you have to enter an another double digit number & then I'll do my turn ,then you & at\nlast the fifth turn you have to enter another number(double digit). What the surprise is that I'm gonna tell you thesum of \nall these 5 numbers just after you entered the first and at the end of the program you'll gonna see the same\nsum of five numbers which I told above just after seeing the first. Hope you'll enjoy this game!\n********** ")
print("WELCOME TO SUM GAME")  # It's just way of starting a game
x = int(input("enter a number: "))  # In this line, we took the first number from the player
print("I think the whole sum  will be... it's only my guess......")  # I'm guessing the whole sum
time.sleep(2)
# I import time & uses it for delay in execution the number of secnds which we wanna delay is written in brackets.
print(x + 198 ) # It's the part of a trick.
print("Your turn again")   # This statement is indicating the second turn of a player.
y = int(input("enter a number: "))  # It's the 2nd turn of a player to enter a number.
print("my turn now")  # This statement is indicating my turn!
z = 99 - y  # This step contains a arithmetic expression of variables.
print(z)  # This expression is showing that by using  print command I wanna display the number I choose.
print("loading.....")
time.sleep(2)
print("your turn once again")  # This line is indicating the turn of player
a = int(input("enter a number: "))  # This line is indicating the turn of a player to enter a number for the 3rd time.
print("now my turn")  # This line is indicating my turn.
time.sleep(2)
b = 99 - a  # This step contains a arithmetic expression of variables.
print(b)  # This statement means to display a number which I choose.
time.sleep(2)
print("THE SUM OF ABOVE FIVE NUMBERS IS")  # In this statement we print a sentence.
sum = x + y + z + a + b  # In this We're doing the sum of all five numbers.
time.sleep(2)
print(sum)  # here we display the total sum of all five numbers.
time.sleep(2)
print("Yayy!!!My guess was right")  # here we print a statement at the end of a game.
print("THE END")
