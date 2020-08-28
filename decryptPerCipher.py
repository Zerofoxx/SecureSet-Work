#!/usr/bin/python3

import pyperclip
import math

key = input("Enter your key here: ")
message = input("Enter your message here: ")
message = message.replace(" ", '')


def thisWayStupid():
    sortedKey = sorted(key)
    theKey = []
    for i in range(len(key)):
        theKey.append(int(sortedKey.index(key[i])))
        
    return theKey

theKey = thisWayStupid()

def splitMessage():
    splitCount = 0
    splitList = []
    for i in range(math.ceil(len(message) / 7)):
        listInList = message[(splitCount) : (splitCount + 7)]
        splitList.append(listInList)
        splitCount += 7
    for j in range(len(splitList)):
        if len(splitList[j]) == 7:
            pass
        else:
            times = 7 - len(splitList[j])
            for k in range(times):
                splitList[j] += 'Q'
                
    return splitList

splitMessage = splitMessage()

def indexer():
    counter = 0
    tempKey = sorted(key)
    newKey = {}
    for i in range(len(key)):
        newKey[i] = 0
    for j in key:
        newKey[counter] = tempKey.index(j)
        counter += 1
    return newKey

newKey = indexer()
print(newKey)


def myDogScrambles():
    encrypted = []
    for i in splitMessage:
        temp = list(range(7))
        counter = 0
        for j in i:
            temp.insert(newKey.get(counter),j)
            temp.pop(newKey.get(counter) + 1)
            counter += 1
        encrypted.append(temp)
        counter -= 7
    return encrypted

myDogScrambles = myDogScrambles()
print(myDogScrambles)

def iToldYouSo():
    finalMessage = ''
    for i in myDogScrambles:
        finalMessage += ''.join(i)
    return finalMessage

print("Heres your decryped message: ", iToldYouSo())