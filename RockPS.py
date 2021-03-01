# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:32:29 2021

@author: Roger
"""

import keyboard as kyb
import random as rdm
import sys


def playRPS(repeat):
    ply = input("Play " + repeat + "Rock, Paper, Scissors? - [y/n]")
    if ply == "y":
        print("\npress\n'r' for Rock\n'p' for Paper or\n's' for Scissors\n")
        while True:
            if kyb.is_pressed('r'):
                usrC = 1
                print("You chose ROCK")
                chooseRPS(usrC)
            elif kyb.is_pressed('p'):
                usrC = 2
                print("You chose PAPER")
                chooseRPS(usrC)
            elif kyb.is_pressed('s'):
                usrC = 3
                print("You chose SCISSORS")
                chooseRPS(usrC)
            else:
                pass
    elif ply == "n":
        print("\nOK... thanks for playing.\nGodbye")
        sys.exit()
    else:
        print("Sorry... your answer not recognised...")
        playRPS("")


def chooseRPS(usrC):
    cmpC = rdm.randint(1, 3)
    if cmpC == 1:
        print("I chose ROCK")
        whoWon(cmpC, usrC)
    elif cmpC == 2:
        print("I chose PAPER")
        whoWon(cmpC, usrC)
    else:
        print("I chose SCISSORS")
        whoWon(cmpC, usrC)


def whoWon(cmpC, usrC):
    if cmpC == usrC:
        print("                It's a DRAW")
        playRPS("another game of ")
    elif (usrC == 1 and cmpC == 2) or (usrC == 2 and cmpC == 3) or (usrC == 3 and cmpC == 1):
        print("                I Won")
        playRPS("another game of ")
    else:
        print("                YOU Won")
        playRPS("another game of ")


print("""\n     Rock, Paper, Scissors is a game where two players choose
      one of 'rock', 'paper' or 'scissors' at the same time and
      then decide a winner according to the rules:
          ROCK beats Scissors
          PAPER beats Rock &
          SCISSORS beats Paper
       if both players choose the same symbol the game is a draw.""")
playRPS("")
