import random

def play():
    user = input("What's your choice? (r - rock, p - paper, s - scissors)\n")
    opponent = random.choice(["r", "p", "s"])

    if user == opponent:
        print("It's a tie")
        return False

    return you_win(user, opponent)


def you_win(user, opponent):
    if ((user == 'r' and opponent == 's') or
        (user == 'r' and opponent == 'p') or
        (user == 'p' and opponent == 'r')):
        print("YOU WON")
        return True

    print("You lost")
    return False

play()

