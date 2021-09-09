import random


# def rps():
#     user = input(
#         "choice? \n'r' for rock. \n's' for scissor \n'p' for paper \n")
#     comp = random.choice(['r', 'p', 's'])

#     if user == comp:
#         return "it's a tie"

#     if win(user, comp):
#         return (f'You won!. Comp chose {comp}')

#     return (f'You lost. Comp chose {comp}')


# def win(player, opponent):
#     if (player == 'r' and opponent == 's') \
#             or (player == 's' and opponent == 'p') \
#             or (player == 'p' and opponent == 'r'):
#         return True

    # return play()
# print(rps())

    # return play()s

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


def win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(rps())
