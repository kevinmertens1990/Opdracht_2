#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de Valori FST intake opdracht. Werk zorgvuldig en netjes, succes!"
motivationLetter = "In de afgelopen maand tijdens de Masterclass is het mij duidelijk geworden dat mijn interesse ligt bij testautomatisering en programmeren. Gecombineerd met mijn communicatie skills en achtergrond in sales en marketing denk ik dat dit een goede match zou zijn."

def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    exercise = motivationLetter
    return exercise

if len(welcomeMessage) != 76:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
print(printExercise())
