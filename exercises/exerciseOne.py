#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de Valori FST intake opdracht. Werk zorgvuldig en netjes, succes!"

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    return None

if len(welcomeMessage) != 76:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
