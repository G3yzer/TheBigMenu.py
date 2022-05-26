import random
import os

def Calculator():
    running = True
    while running == True:
        number1 = int(input("\nNUMBER1: "))
        number2 = int(input("\nNUMBER2: "))
        operator = str(input("\nOPERATOR: "))
        
        if operator == "+":
            total = number1 + number2
            print(total)
        elif operator == "*":
            total = number1 * number2
            print(total)
        elif operator == "/":
            total = number1 / number2
            print(total)
        elif operator == "-":
            total = number1 - number2
            print(total)
        else:
            print("error")

        run = input("Would like run again? Y/N \n")
        if run == "N":
            running = False

def Text():
    runningText = True
    while runningText:

        try:
            menuChoice = int(input("======MENU======\n\n 1. Creat a text file\n 2. Write to a text file\n 3. Append to a text file\n 4. Delete a text file\n 5. exit\n"))
            
            if menuChoice == 1:
                CreateText()
            elif menuChoice == 2:
                WriteText()
            elif menuChoice == 3:
                AppendText()
            elif menuChoice == 4:
                DeleteText()
            elif menuChoice == 5:
                BigMenu()
        except ValueError:
            print("Invalid Input.")
            Text()
        

def CreateText():
    FileName = input("What is the name of the file you would like to create?\n")
    f= open(FileName, "w+")
    textToWrite = input("What would you like to write to the text file?\n")
    f.write(textToWrite)
    f.close

def WriteText():
    FileName = input("What is the name of the file you would like to write to?\n")
    f= open(FileName, "w+")
    textToWrite = input("What would you like to write in the text file?\n")
    f.write(textToWrite)
    f.close

def AppendText():
    FileName = input("What is the name of the file you would like to append to?\n")
    f= open(FileName, "a+")
    textToWrite = input("What would you like to add to the text file?\n")
    f.write(textToWrite)
    f.close

def DeleteText():
    FileName = input("What is the name of the file you would like to delete?\n")
    os.remove(FileName)

def BigMenu():
    runningBigMenu = True
    while runningBigMenu:

        try:
            BigMenuChoice = int(input("======THE BIG MENU======\n\n 1. Calculator\n 2. Text files\n"))
            
            if BigMenuChoice == 1:
                Calculator()
            elif BigMenuChoice == 2:
                Text()
            elif BigMenuChoice == 3:
                exit()

        except ValueError:
            print("Invalid Input.")
            BigMenu()

BigMenu()