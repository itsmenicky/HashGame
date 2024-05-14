import os
import time
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
        jogada = input(f"\u001b[34m Player's {names['x']} move: ")
        jogar(jogada, 'x')
        player = 'o'

    elif player == 'o':
        jogada = input(f"\u001b[33m Player's {names['o']} move: ")
        jogar(jogada, 'o')
        player = 'x'
    
    
    renderTable()


    if(checkGame(game) and checkGame(game) == 'x'):
        ganhou('x')
        gameIsOver = True
    elif(checkGame(game) and checkGame(game) == 'o'):
        ganhou('o')
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

        if playAgain == 's' or playAgain == 'sim':
            clearTable()
            renderTable()
            runGame()
        elif playAgain == 'n' or playAgain == 'nao':
              os.system('cls')
              print("exiting...")
              break
              SystemExit
        
runGame()