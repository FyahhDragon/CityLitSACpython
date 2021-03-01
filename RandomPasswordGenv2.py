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


def beginGen():
    begin = input("""
              Would you like to generate some free passwords?
              [y/n]: """)
    if begin == "y":
        # call length configure function
        configPWlength()
    elif begin == "n":
        # exit program
        print("""
              Thank you for using myPWORD password generator.
              Goodbye.
              """)
    else:
        # catch exception
        print("""Sorry... answer not recognized.
              Please try again.
              """)
        beginGen()


def configPWlength():
    pwLength = input("""
    How many characters would you like in your passwords?
    [12 to 128]: """)
    try:
        # Convert it into integer
        pwLength = int(pwLength)
        if 12 <= pwLength <= 128:
            numberPW(pwLength)
        else:
            print("""
              Sorry... answer not between 12 and 128.
              Please try again.
                  """)
            configPWlength()
    except ValueError:
        try:
            # Convert it into float
            pwLength = float(pwLength)
            print("""
              Sorry... answer not an Integer.
              Please try again.
                  """)
            configPWlength()
        except ValueError:
            print("""
                  Sorry... answer is not a Number.
                  Please try again.
                  """)
            configPWlength()


def numberPW(pwLength):
    pwAmount = input("""
    How many passwords would you like?
    [1 to 99]: """)
    try:
        # Convert it into integer
        pwAmount = int(pwAmount)
        if 1 <= pwAmount <= 99:
            charPWset(pwLength, pwAmount)
        else:
            print("""
              Sorry... answer not between 1 and 99.
              Please try again.
                  """)
            numberPW(pwLength)
    except ValueError:
        try:
            # Convert it into float
            pwAmount = float(pwAmount)
            print("""
              Sorry... answer not an Integer.
              Please try again.
                  """)
            numberPW(pwLength)
        except ValueError:
            print("""
                  Sorry... answer is not a Number.
                  Please try again.
                  """)
            numberPW(pwLength)


def charPWset(pwLength, pwAmount):
    setChar = input("""
    what characters would you like to use in your passwords?

    for lowercase letters only - enter[l]:
    for UPPERCASE letters only - enter[u]:
    for lowercase & UPPERCASE letters only - enter[lu]:
    for Alpa-numeric charracters only - enter[an]:
    for Alpa-numeric charracters & Symbols - enter[s]:
    """)
    if setChar == "l":
        charStart = 1
        charLimit = 26
        prntPWlist(pwLength, pwAmount, charStart, charLimit)
    elif setChar == "u":
        charStart = 27
        charLimit = 52
        prntPWlist(pwLength, pwAmount, charStart, charLimit)
    elif setChar == "lu":
        charStart = 1
        charLimit = 52
        prntPWlist(pwLength, pwAmount, charStart, charLimit)
    elif setChar == "an":
        charStart = 1
        charLimit = 62
        prntPWlist(pwLength, pwAmount, charStart, charLimit)
    elif setChar == "s":
        charStart = 1
        charLimit = 70
        prntPWlist(pwLength, pwAmount, charStart, charLimit)
    else:
        # catch exception
        print("""Sorry... answer not recognized.
              Please try again.
              """)
        charPWset(pwLength, pwAmount)


def genChar(charStart, charLimit):
    """generates a random character from charSet dictionary and stores it
    in the variable char."""
    char = charSet[random.randint(charStart, charLimit)]
    return char


def genPW(pwLength, charStart, charLimit):
    """ generates a 12 to 128 (pwLength) character password from 'charSet'
    dictionary and stores it in variable newPW."""
    newPW = ""
    i = 1
    while i <= pwLength:
        newChar = genChar(charStart, charLimit)
        newPW = newPW + newChar
        i += 1
    return newPW


def genPWlist(pwLength, pwAmount, charStart, charLimit):
    """ generates 1 to 99 (pwAmount) unique passwords using genPW() function
    and stores them in a list pwList."""
    pwList = []
    j = 1
    while j <= pwAmount:
        nextPW = [genPW(pwLength, charStart, charLimit)]
        pwList = pwList + nextPW
        j += 1
    return pwList


def prntPWlist(pwLength, pwAmount, charStart, charLimit):
    """ calls genPWlist() function and stores list in variable pws, then
    prints the individual elements on new lines. Then asks if another list
    is required and handles input from user."""
    print("\nHere is your list of " + str(pwAmount) + " passwords:\n")
    pws = genPWlist(pwLength, pwAmount, charStart, charLimit)
    ii = 0
    while ii < len(pws):
        print(str(ii+1)+": "+pws[ii])
        ii += 1
    answer = input("""would you like another list of passwords?
                   [y/n]: """)
    if answer == "y":
        configPWlength()
    else:
        print("""
              Thank you for using myPWORD password generator.
              Goodbye.
              """)


print("""welcome to myPWORD password generator.

Here you can select:
1. A password length from 12 to 128.
2. How many passwords to generate, from 1 to 99.
3. Options for which characters to include in the password.
""")
beginGen()
