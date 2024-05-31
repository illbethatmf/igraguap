import random
#Nazhachenie peremennix dlya vixoda iz cikla
igrok_ball = 0
komputer_ball = 0
while (komputer_ball<3) and (igrok_ball<3) :
    #Vibor igroka
    igrok = int(input("Choose Rock (1), Scissors (2) or Paper (3)? "))
    #Vibor komputera
    komputer = random.randint(1, 3)
    if komputer == 1:
        print("Computer choses rock")
    if komputer == 2:
        print("Computer choses scissors")
    if komputer == 3:
        print("Computer choses paper")
        #Podscet ballov
    if igrok == komputer:
        komputer_ball = komputer_ball
        igrok_ball = igrok_ball
    elif (igrok==1 and komputer == 2) or (igrok==2 and komputer == 3) or (igrok==3 and komputer == 1) :
         igrok_ball +=1
    elif igrok > 3:
        #esli vibor igroka ne podxodit po usloviy igri
        print("It doesnt work like this")
    else:
        komputer_ball +=1
        #Podscet pobeditelya
if komputer_ball<igrok_ball:
    print("You won")
elif igrok_ball<komputer_ball:
    print("You lost")
elif komputer_ball==igrok_ball:
    print("Spare")
print("Count", igrok_ball, ":", komputer_ball, "(You : Computer)")
