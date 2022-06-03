from random import randint

#moves for the player
moves = ["R", "P", "S"]

while True:
    computer = moves[randint(0,2)]
    player = input('Please werey input your choice: ').lower()
    if player=='end':
        print('so you don japa?')
        break
    
    elif computer==player:
         print ('Tie')
    elif player=='rock':
        if computer=="paper":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
        else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    elif player=="paper":
       if computer=="Scissors":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
       else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    elif player=="scissors":
       if computer=="rock":
            print('computer picks:',computer,'player picks: ',player)
            print('you lose ', computer ,'beats', player)
       else:
            print('computer picks:',computer,'player picks: ',player)
            print('you win ', player ,'beats', computer)
    else:
        print('ohmo write correct english na...pick ,R ,S , or ,P')