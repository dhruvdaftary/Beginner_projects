import random
a=[0]
def comp_try():
    num = random.randint(1,2)
    number = a[-1]
    if num == 1:
        number += 1
        a.append(number)
    if num == 2:
        number += 1
        a.append(number)
        number += 1
        a.append(number) 
    print("The computer played {} places.".format(num)) 
    print(a)       
def user_try():
    v = True
    while v:
        num = int(input("How many place do you want to enter (1/2): "))
        number = a[-1]
        if num == 1:
            number += 1
            a.append(number)
            v = False
        elif num == 2:
            number += 1
            a.append(number)
            number += 1
            a.append(number) 
            v = False
        else:
            print("Invalid Input")
            continue
    print(a)
played = input("Enter your name: ")
player = None
ans = (input("Do you want to start the game: ")).lower()
if ans == "yes":  
    while True:
        user_try()
        player = played
        if len(a) >= 22:
            break 
        else:
            pass
        comp_try()
        player = "Computer"
        if len(a) >= 22:
            break     
        else:
            pass   
elif ans == "no":    
    while True:
        comp_try()
        player = "Computer"
        if len(a) >= 22:
            break     
        else:
            pass   
        user_try()
        player = played
        if len(a) >= 22:
            break 
        else:
            pass
else:
    print("Invalid Input")
print("{} wins".format(player))
