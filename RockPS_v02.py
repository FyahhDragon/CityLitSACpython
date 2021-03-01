# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:32:29 2021

@author: Roger
"""
import keyboard as kyb
import random as rdm
import sys

choice = ["Rock", "Paper", "Scissors"]


def playRPS(repeat):
    ply = input("Play " + repeat + "Rock, Paper, Scissors? - [y/n]")
    if ply == "y":
        compC = rdm.randint(0, 2)
        print("\npress\n'r' for Rock\n'p' for Paper or\n's' for Scissors\n")
        while True:
            if kyb.is_pressed('r'):
                usrC = 0
                whoWon(compC, usrC)
            elif kyb.is_pressed('p'):
                usrC = 1
                whoWon(compC, usrC)
            elif kyb.is_pressed('s'):
                usrC = 2
                whoWon(compC, usrC)
    elif ply == "n":
        print("\nOK... thanks for playing.\nGodbye")
        sys.exit()
    else:
        print("Sorry... your answer not recognised...")
        playRPS("")


def whoWon(compC, usrC):
    if compC == usrC:
        print("You: ", choice[usrC], "\nMe: ", choice[compC], "\n           ...It's a DRAW")
    elif (usrC == 0 and compC == 1) or (usrC == 1 and compC == 2) or (usrC == 2 and compC == 0):
        print("You: ", choice[usrC], "\nMe: ", choice[compC], "\n           ...I Won")
    else:
        print("You: ", choice[usrC], "\nMe: ", choice[compC], "\n           ...YOU Won")
    playRPS("another game of ")


print("""\n     Rock, Paper, Scissors is a game where two players choose
      one of 'rock', 'paper' or 'scissors' at the same time and
      then decide a winner according to the rules:
          ROCK beats Scissors
          PAPER beats Rock &
          SCISSORS beats Paper
       if both players choose the same symbol the game is a draw.""")
playRPS("")
