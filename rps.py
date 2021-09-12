import random

x = "Bry"

def rps():
    user = input(f"Hey friend! make your choice? \n'r' for rock. \n's' for scissor \n'p' for paper \n")
    comp = random.choice(['r', 'p', 's'])
    # random.choice([1,2,'5'])

    if user == comp:
        return (f"Hey Buddy, it's a tie. comp chose {comp}")
        # print('checking')

    if win(user, comp):
        return (f'You won!. Comp chose {comp}')

    print(f'You lost. Comp chose {comp}')
    
#     this file has been modified . feel free to add or remove codes here. 
# Test question ,,,,, loop the game till a win is declared.... 


def win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(rps())
