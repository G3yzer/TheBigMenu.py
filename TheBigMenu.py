from ast import Delete
import random
import os
import time

def Calculator():
    runningCalc = True
    while runningCalc:
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
        if run.upper() == "N":
            runningCalc = False
            BigMenu()

def Text():
    runningText = True
    while runningText:

        try:
            menuChoice = int(input("\n======TEXT FILES MENU======\n\n 1. Create a text file\n 2. Write to a text file\n 3. Read from a text file\n 4. Append to a text file\n 5. Delete a text file\n 6. exit\n"))
            
            if menuChoice == 1:
                CreateText()
            elif menuChoice == 2:
                WriteText()
            elif menuChoice == 3:
                ReadText()
            elif menuChoice == 4:
                AppendText()
            elif menuChoice == 5:
                DeleteText()
            elif menuChoice == 6:
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

def ReadText():
    FileName = input("What is the name of the file you would like to read from?\n")
    f= open(FileName, "r")
    print("\nHere are the contents of your file:")
    print(f.read())
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

def RandomNumber():
    print("What are the numbers you'd like a random number between")
    RandomNumberBottom = int(input("Lowest?\n"))
    RandomNumberTop = int(input("Highest?\n"))    
    RanNumber = random.randint(RandomNumberBottom, RandomNumberTop)
    print("Finding random number...")
    time.sleep(3)
    print("Your number is " + str(RanNumber))
    time.sleep(2.5)

def exiting():
    print("\nur gay")
    exit()




def BigMenu():
    runningBigMenu = True
    while runningBigMenu:

        try:
            BigMenuChoice = int(input("\n======THE BIG MENU======\n\n 1. Calculator\n 2. Text files\n 3. Random number\n 4. Exit\n"))
            
            if BigMenuChoice == 1:
                Calculator()
            elif BigMenuChoice == 2:
                Text()
            elif BigMenuChoice == 3:
                RandomNumber()
            elif BigMenuChoice == 4:
                exiting()

        except ValueError:
            print("Invalid Input.")
            BigMenu()

BigMenu()
