# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:57:46 2021
Long Division Calculator
@author: Roger
"""


def decimals(divisor, dividend, places):
    """
    Long Division (of NATURAL numbers???) Calculator mechanics

    """
    remainder = 1
    length = 0

    while (remainder != 0 or length < places):
        length += 1
        if length > places:
            break
        # Floor division is the // operator
        print("check 1 rem: ", remainder)
        quotient = dividend // divisor
        print("check 2 quot: ", quotient)
        remainder = dividend % divisor
        print("check 3 rem: ", remainder)

        if remainder < divisor:
            print("check 4-A rem < divsor: ", True, "\nrem: ", remainder, "\ndivdnd: ", dividend, "\ndivsor: ", divisor)
            dividend = remainder * 10
        else:
            print("check 4-B rem > divsor: ", False, "\nrem: ", remainder, "\ndivdnd: ", dividend, "\ndivsor: ", divisor)
            dividend = remainder
        yield quotient


def main(divisor, dividend, places):
    final = ["result: "]
    for digit in decimals(divisor, dividend, places):
        print("                        digit: ", digit)
        final.append(digit)
    print(final[0], final[1], ".", final[2: len(final)])


dividend = int(input("please enter the number to divide\n(preferably not zero): "))
divisor = int(input("please enter the number to divide by\n(DEFINITELY not zero): "))
places = int(input("please enter the number of decimal places for your result: ")) + 1
main(divisor, dividend, places)
