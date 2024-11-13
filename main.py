import math
def frontPage():
    print("\n")
    print("hello world")
    print()
    print("Hello User, this is a program meant to translate Base 10 (decimal) integers into other bases")
    input("please press enter to continue")
def defineBase(decNum):
    base = int(input("Please enter a positive whole number that is less then 10 that will be the base that " + str(decNum) + " is translated to: "))
    return base

def getDecNumToTranslate():
    decNum = int(input("Please input a postive whole number to be translated from Base 10 to another base: "))
    return decNum

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