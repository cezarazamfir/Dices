import random

print("BARBUT")


sum = 100 
print('You have 100 euros.')

while (sum!=0):
    
    bet = int(input("\n Choose your bet: \n"))

    while bet>sum:
        bet = int(input('The bet must be smaller of equal to your current sum: '))


        
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print('Computer hand:', dice_1, dice_2)
    computer = dice_1 + dice_2
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    print('Your hand:    ', dice_1, dice_2)
    player = dice_1 + dice_2

    if computer > player: 
        print('You lost!')
        sum = sum - bet
    elif computer < player: 
        print('You won!')
        sum = sum + bet
    else: 
        print('It s a tie!')
        
    print('Your current sum:', sum)

print('\nYou don t have any money left')
        

    



