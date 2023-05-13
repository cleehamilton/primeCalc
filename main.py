##VS 1.0 **kaff1n8t3d
#https://byjus.com/maths/how-to-find-prime-numbers/
# test primes 1 - 1000 and checked with data from https://byjus.com/maths/prime-numbers-from-1-to-1000/#:~:text=The%20prime%20numbers%20from%201%20to%20200%20are%3A,%2C%20193%2C%20197%2C%20199. 
limit2Run = 5 ##1000000000 ##sets a stopping point by length of number
verboseOutput = 0 ## 1 will print steps involved; 0 will not print steps.

if verboseOutput == 1: ## echo the Settings
    print('\nVerbose Output set to: On')
    print('Limit to run (number length) set to:', limit2Run)
    

import os
from ast import Break
from math import sqrt
primeFile = "primes.txt" ## preloaded with "2\n"
new_path_base = __file__.rstrip(os.path.basename(__file__))
primeFileLocation = f"{new_path_base}{primeFile}"

def searchNextPrime(): ## Search for next prime
    number = GetLastNumber() #start with the last prime found
    
    if verboseOutput == 1:
        print("\nStarting with Prime No.", number)

    j = len(str(number))#get the length of the number
    #print(j)

    while j < limit2Run: ##test until limit is reached
        if number == 2: ## Outside of 2 & 3, no prime has been found consecutively
            number += 1
            if verboseOutput == 1:
                print("\n:: New Number to test is", number,"::")
                print('Length of starting Prime is:', j)
        else:
            number += 2 ## Advance the number to the next number to search
            if verboseOutput == 1:
                print("\n:: New Number to test is", number,"::")
                print('Length of starting Prime is:', j)

        if primeTest1(number) == True and primeTest2(number) == True and primeTest3(number) == True: ## Run Prime Tests
            print("--{",number, "is Prime")
            #write Prime to file
            writeToFile("a",primeFileLocation,str(number) + "\n")
            if verboseOutput == 1:
                print("   ",number, "has been added to " + primeFile + " file.")
        else:
            print(number, "is NOT Prime /-|**|-\\")
            Break

        j = len(str(number + 2)) # gets the length of the new number for loop

def GetLastNumber():## Grab the last prime number found
    if verboseOutput == 1:
        print("Getting last number in prime file...")
    #open file
    f = open(primeFileLocation,"r")
    #read file
    with f as a_file:
        for line in a_file:
            numberRaw = line.strip()
            #print(numberRaw)

    #close file
    f.close()
    numberSplt = numberRaw.strip('\n').split(',')
    #print(numberSplit)
    numberSplit = int(numberSplt[0])
    if verboseOutput == 1:
        print('  Last Prime Number recorded is: ', numberSplit)
    return numberSplit
# number = GetLastNumber()
# print(number)



def primeTest1(number):#test last digit for even numbers - Primes do not end in even numbers but are always an even distance between
    if verboseOutput == 1:
        print("\nTest 1")
        print("  Testing", number, "for ending in even digit...")
    qualifier = number % 2
    if qualifier == 0: #or qualifier == 2 or qualifier == 4 or qualifier == 6 or qualifier == 8:
        if verboseOutput == 1:
            print("  ",number, "ends in an even digit. It can't be Prime.")
            print("  Failed Test 1.\n")
        return False
    else:
        if verboseOutput == 1:
            print("  ",number, "is not even.")
            print("  Passed Test 1.\n")
        return True
#print(primeTest1(26))

def primeTest2(number):#test sum of digits divisible by 3? return True... meaning it does not divide by three.
    if verboseOutput == 1:
        print("Test 2")
        print("  Testing", number, "for add multidigit and dividing by three...")
    x = 0
    numberSliced = str(number)
    #print(numberSliced[0])
    for xr in numberSliced:
        x += int(xr)
    if x % 3 == 0:
        if x/3 == 1:
            if verboseOutput == 1:
                print("  The sum of the digits is",x,". Three is a prime.")
                print("  Passed Test 2.\n")
            return True
        else:
            if verboseOutput == 1:
                print("  The sum of the digits from", number, "is",x,"and is divisible by 3. It can't be Prime.")
                print("  Failed Test 2.\n")
            return False
    else:
        if verboseOutput == 1:
            print("  The sum of the digits from", number, "is",x,"and is not divisible by 3.")
            print("  Passed Test 2.\n")
        return True
#print(primeTest2(27))

def primeTest3(number): #test divisible by previous primes below SQRT True meaning not divisible by previous primes
    if verboseOutput == 1:
        print("Test 3")
        print("  Testing", number, "for division of previous primes below it's squareroot...")
    squareRoot = sqrt(number)
    if verboseOutput == 1:
        print("  Square root of", number, "=", int(squareRoot))
    x = int(squareRoot)
    test = get_primes(x,number)
    if verboseOutput == 1:
        if test == True:
            print("  Passed Test 3.\n")
        else:
            print("  The number", number, "is divisiable by a previous prime, below it's squareroot.")
    return test


def get_primes(x,number):
    #open file
    f = open(primeFileLocation,"r") 
    #read file
    readFile = f.readline()
    readFileOp = 1
    testcase = False
    while readFileOp == 1: # loop through line items in file and check for divisibility until square root is found.
        #print(readFile)
        readFile = readFile.strip('\n')
        testPrime = int(readFile)

        if testPrime <= x:# line from file is less than or equal to SQrt
            if verboseOutput == 1:
                print("  Prime #",testPrime)
                print("  Test entered...")
            ## Do the test
            if number >= 4 and number % testPrime != 0:
                if verboseOutput == 1:
                    print("    Modulus =", number % testPrime," (",number, "modulus", testPrime ,"! = 0)")
                    print("    Passed")
                testcase = True
                readFileOp = 1 ## Continue file Loop
                readFile = f.readline()
            else:
                testcase = False
                readFileOp = 0
                if verboseOutput == 1:
                    print("  Fail Test 3: because number % testPrime  = 0 (",number % testPrime, ")")
        elif number == 3:# safety net for prime 3
            testcase = True
            readFileOp = 0 # End file loop
        else:## it's larger; break loop.
            readFileOp = 0 # End file loop
    #close file
    f.close()
    return testcase

#print(primeTest3(225))# False
#print(primeTest3(227))# True


def writeToFile(method,fileName,data):
    ## open File
    f = open(fileName,method)
    ## Read/Write file
    f.write(data)
    ## Close file
    f.close()

if __name__ == "__main__":  
    #run Prog
    searchNextPrime()  