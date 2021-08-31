import random

numbertry = int(input("Enter the number of tries you want: "))
lowerlimit,upperlimit = (input("Enter the range from which you want to choose (leave a blank btw the nos): ")).split()
lowerlimit,upperlimit = int(lowerlimit),int(upperlimit)
number = random.randint(lowerlimit,upperlimit)
trynum = 0
print(number)
while numbertry > trynum:
    trynum = trynum + 1
    guess = int(input(("Guess a number between {} and {}: ").format(lowerlimit,upperlimit)))
    if guess == number:
        print("Congrats you have guessed the correct number in {} tries.".format(trynum))
        print("Thanks for playing.")
        break
    else:
        if number > guess:
            if number - guess >= 10:
                print("You have guessed too low")
            elif number - guess < 10:
                print("You have guessed a little low")
        elif guess > number:
            if guess - number >= 10:
                print("You have guessed too high")
            elif guess - number < 10:
                print("You have guess a little high")
else:
    print("You have exhausted your number of tries \nThe right answer is {}".format(number))
