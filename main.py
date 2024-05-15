import os
import time
import sys
from functions import *

os.system('cls')
print("\u001b[36m                                     \-->HashGame<--/\n\n")
time.sleep(2)
os.system('cls')

print("                                 \u001b[31m||  X  ||     ||  O  ||\n")
time.sleep(1)
print("                                 \u001b[32m||-----||-----||-----||\n")
time.sleep(1)
print("                                 \u001b[31m||  O  ||  X  ||  O  ||\n")
time.sleep(1)
print("                                 \u001b[32m||-----||-----||-----||\n")
time.sleep(1)
print("                                 \u001b[31m||     ||  O  ||  X  ||\n")
time.sleep(2)
os.system('cls')

"""
Function responsible for executing the game
"""
def runGame():
  gameIsOver = False
  renderTable()

  namePlayer1 = input("\u001b[34m Player1 name (X): ")
  namePlayer2 = input("\u001b[33m Player2 name (O): ")
  
  names = {'x': namePlayer1, 'o': namePlayer2}
  
  playing = True
  player = 'x'


  while (playing):
    allFilled = False
    if player == 'x':
        move = input(f"\u001b[34m Player's {names['x']} move: ")
        play(move, 'x')
        player = 'o'

    elif player == 'o':
        move = input(f"\u001b[33m Player's {names['o']} move: ")
        play(move, 'o')
        player = 'x'
    
    
    renderTable()


    if(checkGame(game) and checkGame(game) == 'x'):
        win('x')
        gameIsOver = True
    elif(checkGame(game) and checkGame(game) == 'o'):
        win('o')
        gameIsOver = True
    
    for line in game:
            for item in line:
                if item != ' ':
                    allFilled = True
                else:
                    allFilled = False

    if allFilled:
        print(f"\u001b[31mIt's a draw!")
        gameIsOver = True
        
    if gameIsOver:
        playAgain = input('Play again? (Y/Yes - N/No)-> ').lower()

        if playAgain == 'y' or playAgain == 'yes':
            clearTable()
            renderTable()
            runGame()
            break
        elif playAgain == 'n' or playAgain == 'no':
              os.system('cls')
              print("exiting...")
              sys.exit()
        else:
            print("invalid option! exiting...")
            sys.exit()
        
runGame()