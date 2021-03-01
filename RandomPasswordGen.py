# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:49:02 2021

@author: Roger
"""

import random

charSet = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h",
           9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o",
           16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v",
           23: "w", 24: "x", 25: "y", 26: "z", 27: "A", 28: "B", 29: "C",
           30: "D", 31: "E", 32: "F", 33: "G", 34: "H", 35: "I", 36: "J",
           37: "K", 38: "L", 39: "M", 40: "N", 41: "O", 42: "P", 43: "Q",
           44: "R", 45: "S", 46: "T", 47: "U", 48: "V", 49: "W", 50: "X",
           51: "Y", 52: "Z", 53: "0", 54: "1", 55: "2", 56: "3", 57: "4",
           58: "5", 59: "6", 60: "7", 61: "8", 62: "9", 63: "!", 64: "£",
           65: "$", 66: "%", 67: "&", 68: "#", 69: "@", 70: "?"}


def genChar():
    """generates a random character from charSet dictionary and stores it
    in the variable char."""
    char = charSet[random.randint(1, len(charSet))]
    print(len(charSet))
    return char


def genPW():
    """ generates a 12 character password from 'charSet' dictionary
    and stores it in variable newPW."""
    newPW = ""
    i = 1
    while i <= 12:
        newChar = genChar()
        newPW = newPW + newChar
        i += 1
    return newPW


def genPWlist():
    """ generates 10 unique passwords using genPW() function and stores them
    in a list pwList."""
    pwList = []
    j = 1
    while j <= 10:
        nextPW = [genPW()]
        pwList = pwList + nextPW
        j += 1
    return pwList


def prntPWlist():
    """ calls genPWlist() function and stores list in variable pws, then
    prints the individual elements on new lines. Then asks if another list
    is required and handles input from user."""
    print("\nHere is your list of 10 passwords:\n")
    pws = genPWlist()
    ii = 0
    while ii < len(pws):
        print(str(ii+1)+": "+pws[ii])
        ii += 1
    answer = input("would you like another list of 10 passwords? (y/n)\n")
    if answer == "y":
        prntPWlist()
    else:
        print("Thank you for using this password generator. Goodbye.")


prntPWlist()  # start- prints initial list and asks if further list required
