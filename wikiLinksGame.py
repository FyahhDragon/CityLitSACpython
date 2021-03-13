# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:44:24 2021

@author: Roger Dunn

if you're short on ideas.... try:

    https://en.wikipedia.org/wiki/Hammerhead_shark
"""

import requests
import sys


def getNext20(url):
    s = requests.session()
    reply = s.get(url)
    rawText = reply.text
    rawText = rawText.lower()
    linkSplit = rawText.split("href=")
    links20 = []
    for k in linkSplit:
        link = k.split("\"")
        if("http" in link[1]):
            links20.append(link[1])
            if len(links20) > 19:
                addHistory(links20[-1])


def addHistory(url):
    history.append(url)
    if len(history) > 1:
        a = 0
        while a < len(history)-1:
            if history[a] == history[-1]:
                x = 1
                while x < len(history)-1:
                    print(x, ": ", history[x])
                    x += 1
                print("Chain broken\n", history[-1],
                      "\nhas been visited before",
                      "\nYou visited ", x, "new Links")
                sys.exit()
            a += 1
    else:
        getNext20(history[-1])


history = []
startUrl = input("please enter a wikipedia url to start from:\n")
getNext20(startUrl)
