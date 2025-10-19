import datetime
import random as rnd
def draw_board(board):
    print("  " + " ".join([chr(ord('a') + i) for i in range(len(board[0]))]))
    for i, row in enumerate(board):
        print(f"{i + 1} " + " ".join(row))

board = [["." for _ in range(8)] for _ in range(8)]

def mole():
    board[rnd.randint(0,7)][rnd.randint(0,7)] = 'n'


def WHACK(xy):
    y = int(xy[1:]) - 1
    abc = ['a','b','c','d','e','f','g','h']
    x = abc.index(xy[0])
    if board[y][x] == 'n':
        board[y][x] = '.'
        return True
    else:
        return False

playing = True
score = 0


t=5

print('co ordinates are in form xy e.g. a1, press enter to start')
input()
while playing == True:
    mole()
    draw_board(board)

    startTime = datetime.datetime.now()
    xy = input(f"you have {t} seconds WHACK!!!!")
    endTime = datetime.datetime.now()

    time_difference = (endTime - startTime).total_seconds()

    if time_difference > t:
        print(f"You took too long! Game over. You achieved {score} points")
        playing = False
        break
    if WHACK(xy) != True:
        print(f"game over you achieved {score} points")
        playing = False
    score += 1


# RUN GAME.py