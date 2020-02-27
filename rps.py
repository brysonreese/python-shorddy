# Bryson Reese // 2-27-2020
# Wrote this between 9:10AM and 9:53AM while in CS 326
# Go Pack!

import random

userInput, cpuAnswer  = "", ""
userWinCount, cpuWinCount = 0, 0
ansDict = {"R": "Rock", "P": "Paper", "S":"Scissors"}

def whoWins(user, cpu):
    if (user == "R" and cpu == "S") or (user == "P" and cpu == "R") or (user == "S" and cpu == "P"):
        return 0
    elif (user == cpu):
        return 2
    else:
        return 1

print("Welcome to rock, paper, scissors!")
while userInput != "Q":
    while not userInput in ansDict.keys() and userInput != "Q":
        userInput = input("(R)ock, (P)aper, (S)cissors, (Q)uit\nInput choice: ")
    if userInput != "Q":
        cpuAnswer = random.choice(list(ansDict.keys()))
        print("User played " + ansDict[userInput] + "\nCPU played " + ansDict[cpuAnswer])
        outcome = whoWins(userInput, cpuAnswer)
        if outcome == 0:
            print("User wins!\n")
            userWinCount = userWinCount + 1
        elif outcome == 1:
            print("CPU wins!\n")
            cpuWinCount = cpuWinCount + 1
        else:
            print("Draw!\n")
        userInput = ""
        cpuAnswer = ""
        print("User wins: " + str(userWinCount) + "\nCPU wins: " + str(cpuWinCount))