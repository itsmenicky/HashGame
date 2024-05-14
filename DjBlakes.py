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

  namePlayer1 = input("\u001b[34m Nome Player1 (X): ")
  namePlayer2 = input("\u001b[33m Nome Player2 (O): ")
  
  names = {'x': namePlayer1, 'o': namePlayer2}
  
  playing = True
  player = 'x'


  while (playing):
    allFilled = False
    if player == 'x':
        jogada = input(f"\u001b[34m Jogada de {names['x']}: ")
        jogar(jogada, 'x')
        player = 'o'

    elif player == 'o':
        jogada = input(f"\u001b[33m Jogada de {names['o']}: ")
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
        print(f'\u001b[31mDeu velha')
        gameIsOver = True
        
    if gameIsOver:
        playAgain = input('Play again? (S/Sim - N/Nao)-> ').lower()

        if playAgain == 's' or playAgain == 'sim':
            clearTable()
            renderTable()
            runGame()
        elif playAgain == 'n' or playAgain == 'nao':
              os.system('cls')
              print("Fechando DjBlakes...")
              break
              SystemExit
        
runGame()