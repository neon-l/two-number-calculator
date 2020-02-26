import time
while True:
    print("")
    print("#############################################")
    print("##                                         ##")
    print("##          Two Number Calculator          ##")
    print("##                                         ##")
    print("#############################################")
    print("")
    print(" 1 : For Adding")
    print(" 2 : For Substracting")
    print(" 3 : For Multiplying")
    print(" 4 : For Dividing")
    print("")
    userInput=int(input("Select what you want to do : ") )
    if userInput != 4 or userInput !=3 or userInput !=2 or userInput !=1:
        print("")
        print("Warning ** Please Enter the correct number from 1 to 4")
        time.sleep(3)
        continue
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
    print("")
    print ("The result is {} ".format(round(result,5)))
