#!/usr/bin/env python

import string
import random

def generateFile(fileName, chars, lines):
  myFile = open(fileName, 'w')
  currentLine = 0
  writeString = ""
  while currentLine < lines:
    currentChar = 0
    newLine = ""
    while currentChar < chars:
      newLine += random.choice(string.ascii_letters + string.digits +\
                               string.punctuation)
      currentChar += 1
    writeString += newLine + '\n'
    currentLine += 1
  myFile.write(writeString)
  myFile.close()

def main():
    #generate the title, between 10 to 76 characters long
    titleLength = random.randrange(10,76)
    fileName = ""
    while len(fileName) < titleLength:
      fileName += random.choice(string.ascii_letters)
    fileName = "./books/" + fileName + ".txt"

    #get the amount of lines for the random file
    numLines = random.randrange(1,999)

    #get the amount of characters per line for the random file
    charsPerLine = 80 #basic terminal screen of 80 chars wide

    #generate the file
    generateFile(fileName, int(charsPerLine), int(numLines))

main()
