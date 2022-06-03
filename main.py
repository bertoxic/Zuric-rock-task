from random import randint

#moves for the player
moves = ["R", "P", "S"]

while True:
    computer = moves[randint(0,2)]
    player = input('Please werey input your choice, S for scissors, P for paper etc: ').upper()
    if player=='END':
        print('so you don japa?')
        break

    elif computer==player:
         print ('Tie')
    elif player=='R':
        if computer=="P":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
        else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    elif player=="P":
       if computer=="S":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
       else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    elif player=="S":
       if computer=="R":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
       else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    else:
        print('ohmo write correct english na...pick ,R ,S , or ,P or end')