import random

choice = ["rainbow","calm","python","water","school","mobile","player"]
clues = {"rainbow":"It is made up of 7 colours and can be seen on a rainy day",
        "calm":"It is opposite of the word excited",
        "python":"It is a programming language as well as an animal",
        "water":"You drink it and it is necessary for survival",
        "school":"A place where children go to educate themselves",
        "mobile":"A calculator, camera, contact diary all in a single device",
        "player":"A person who plays "}
choice = random.choice(choice)
t = True
while t:
    tries = int(input("Enter the number of tries you want: "))
    if tries > (len(choice)+4):
        t = False
    else:
        print("Choose more number of tries")
        continue
numbertry = 0
p = False
wrong_list = []
correct_word = []
for i in range(len(choice)):
    correct_word.append("_")
while numbertry < tries: 
    if p == False:
        prompt = (input("Do you want clue (yes/no): ")).lower()
        if prompt == "yes":
            print(clues[choice])
            p = True
        elif prompt =="no":
            pass
        else:
            print("Invalid Input")
    guess = input("Guess a character: ").lower()
    if guess.isalpha():
        if guess in wrong_list:
            print("You have already entered this character")
        elif guess not in wrong_list:
            if guess in choice:
                print("You guessed correct this character is present in the word")
                for x in range(len(choice)):
                    if choice[x] == guess:
                        correct_word[x] = choice[x]                                          
            elif guess not in choice:
                print("This character is not there in the word")
                wrong_list.append(guess)
                numbertry += 1
    else:
        print("Enter a single character.")

    word = [i for i in correct_word]
    word = "".join(word)
    print(word)    
    if word == choice:
        print("You have guessed the word")
        print("The word is {}".format(word))
        break    
else:
    print("You have exhausted you number of tries")
print("Thanks for playing")
        
