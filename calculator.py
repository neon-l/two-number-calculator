import time
import sys
print(" 1 : For Adding")
print(" 2 : For Substracting")
print(" 3 : For Multiplying")
print(" 4 : For Dividing")
userInput=int(input("Select what you want to do : ") )

if userInput > 4 or userInput < 1 :
    print("Please Enter the correct number from 1 to 4")
    time.sleep(2)
    sys.exit()
firstNumber = float(input("Enter First Number: "))
secondNumber = float(input("Enter Second Number: "))
if userInput == 1:
    result=firstNumber+secondNumber
elif userInput == 2:
    result=firstNumber-secondNumber
elif userInput == 3:
    result=firstNumber*secondNumber
elif userInput == 4:
    result=firstNumber/secondNumber
time.sleep(1)
print ("The result is {} ".format(result))
