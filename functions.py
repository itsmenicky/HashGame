import os
import time
import numpy as np

game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

"""
Function responsible for changing all list values to an empty string
"""
def clearTable():
  global game
  game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

"""
Function responsible for reading play input and split into column and position, returning the current player's column and position
"""
def readPlay(play):
  col = int(play.split(' ')[1])
  pos = int(play.split(' ')[3])
  if(col > 3 or pos > 3):
    jogada = input("\u001b[31m Digite uma jogada válida (col e line de 1 a 3): ")
    readPlay(jogada)
  return [col-1, pos-1]

"""
Function responsible for receive a Player and print victory screen, mapping player color on each play
"""
def ganhou(jogador):
    os.system('cls')
    # Atribui uma cor para função
    cor = "\u001b[37m"
    if jogador == 'x':
      cor = "\u001b[34m"
    elif jogador == 'o':
      cor = "\u001b[33m"   

    color_mapping = []

    for line in game:
      for item in line:
        if item == jogador:
            color_mapping.append(cor)
        else:
            color_mapping.append('\u001b[37m') # <- branco

    print(f"                              \u001b[32m|**{jogador} venceu!**|\n")
    print(f"                                {color_mapping[0]}{game[0][0].upper()} \u001b[37m |  {color_mapping[1]}{game[0][1].upper()}  \u001b[37m|  {color_mapping[2]}{game[0][2].upper()} \u001b[37m \n")
    time.sleep(1)
    print(f"                             ------|-----|------\n")
    time.sleep(1)
    print(f"                                {color_mapping[3]}{game[1][0].upper()}  \u001b[37m|  {color_mapping[4]}{game[1][1].upper()} \u001b[37m |  {color_mapping[5]}{game[1][2].upper()} \u001b[37m \n")
    time.sleep(1)
    print(f"                             ------|-----|------\n")
    time.sleep(1)
    print(f"                                {color_mapping[6]}{game[2][0].upper()}  \u001b[37m|  {color_mapping[7]}{game[2][1].upper()} \u001b[37m |  {color_mapping[8]}{game[2][2].upper()} \u001b[37m \n")
    time.sleep(2)

"""
Function responsible for checking all lines and diagonals
"""
def checkGame(table):

  #print(table)
  # Checking all lines
  for pos in game:
      if checkLine(pos):
        return checkLine(pos)

  # Checking all columns
  for i in range(len(game)):
    pos = []
    for j in range(len(game)):
      pos.append(game[j][i])
    if checkLine(pos):
      return checkLine(pos)

  # Checking diagonal 1
  diagonal1 = []
  for i in range(len(game)):
    diagonal1.append(game[i][i])
  if checkLine(diagonal1):
    return checkLine(diagonal1)

  # Checking diagonal 2

  diagonal2 = []
  for i in range(len(game)):
    diagonal2.append(game[i][len(table[0])-(i+1)])
  if checkLine(diagonal2):
    return checkLine(diagonal2)

"""
Function responsible for checking if play values are 'x' or 'o'
"""
def checkLine(pos):
  if(all(el == 'x' for el in pos)):
    return 'x'
  elif(all(el == 'o' for el in pos)):
    return 'o'
  return False

"""
Function responsible for receive a play and a Player, split play into column and position and verify if the position are available
"""
def jogar(jogada, jogador):
  if(len(jogada.split(' ')) < 4):
     return
  pos = readPlay(jogada)[1]
  col = readPlay(jogada)[0]
  game_line = game[pos]
  if game_line[col] != " ":
     jogada = input("\u001b[31m Escolha uma posição vazia para jogar: ")
     return jogar(jogada, jogador)
  game[pos][col] = jogador

"""
Function responsible for print table map and current game table
"""
def renderTable():
  os.system('cls')
  print(f"\u001b[33m ==========MAPA DO TABULEIRO==========         \u001b[34m===========GAME==========\n")
  print(f"\u001b[32m            [pos]           ")
  print(f"\u001b[31m      [col]  | 1 | 2 | 3 | \u001b[37m                             {game[0][0].upper()} | {game[0][1].upper()} | {game[0][2].upper()} \n" \
        f"      \u001b[32m       |---|\u001b[37m---|---|                             ---|---|---\n" \
        f"     \u001b[32m        | 1 |\u001b[37m 2 | 3 |                              {game[1][0].upper()} | {game[1][1].upper()} | {game[1][2].upper()} \n" \
        f"      \u001b[32m       |---|\u001b[37m---|---|                             ---|---|---\n " \
        f"     \u001b[32m       | 1 |\u001b[37m 2 | 3 |                              {game[2][0].upper()} | {game[2][1].upper()} | {game[2][2].upper()} \n")