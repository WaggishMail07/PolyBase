import math
letterDecNumValues = {
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "e": 16,
    "g": 17,
    "h": 18,
    "i": 19,
    "j": 20,
    "k": 21,
    "l": 22,
    "m": 23,
    "n": 24,
    "o": 25,
    "p": 26,
    "q": 27,
    "r": 28,
    "s": 29,
    "t": 30,
    "u": 31,
    "v": 32,
    "w": 33,
    "x": 34,
    "y": 35,
    "z": 36
}
def frontPage():
    print("\n")
    print("hello world")
    print()
    print("Hello User, this is a program meant to translate Base 10 (decimal) integers into other bases")
    input("please press enter to continue")


def defineBases(decNum):
    base = 0
    base = int(input("Please enter a positive whole number that is less then 10 that will be the base that " + str(decNum) + " is translated to: "))
    while(base==0 and 10 < base and base < 0):
        base = int(input("please enter a positve whole number less then 10: "))
    return base


def getNumToTranslate():
    inputNum = input("Please input a postive whole number to be translated from Base 10 to another base: ")
    return inputNum


def bigBaseToDec(INPUT, BASE): 
        inputDec = INPUT
        for i in range(0, len(INPUT)):
            inputDec[i] = int(letterDecNumValues[str(INPUT[i])])
            print(str(INPUT[i]) + " --> " + str(inputDec[i]))


def sumDec(INPUT, BASE):
    print("INPUT: " + str(INPUT))
    output = 0

    for i in range(0, len(INPUT)):
        print("INPUT[i]*(BASE**i)=" + str(INPUT[i]*(BASE**i)) + "   | i: " + str(i))
        output+=INPUT[i]*(BASE**i)
    print("sumDec output: " + str(output))
    return output


def translate(DECNUM, BASE):
    # this is the "highest power" or the max number of places/digits the final number can have
    upperPower = 0
    # An array where each spot is one digit
    output=[]
    # loop to determine the value of upperPower, continues as long as the value of the highest digit is less then the inputed number
    while (BASE**upperPower < DECNUM):
        # adds 1 to upperPower
        upperPower+=1
        #adds another place/digit to the output
        output.append(0)
    # debugging output
    print("output: " + str(output))
    print("upperPower: " + str(upperPower))

    # determining the final output
    # loop continues as long as the output is below the required amount
    while (sumDec(output, BASE) < DECNUM):
        # adds one to the first digit in the output array, this is the slowest and easiest method to reach the desired amount
        output[0] += 1
        # checks to find values in the output array that are to high, and changes the values appropriately, EX: in base 10, if the first digit is 10, then it changes the value to 0, and adds 1 to the next digit
        for i in range(0, len(output)):
            if (output[i] >= BASE):
                output[i+1]+=1
                output[i]-=BASE
        print("output: " + str(output) + "   | sum: " + str(sumDec(output, BASE)))
        
frontPage()
DecNum = getDecNumToTranslate()
Base = defineBase(DecNum)
translate(DecNum, Base)