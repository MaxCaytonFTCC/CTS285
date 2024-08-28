# CTS 285
# M1HW
# Max Cayton, Joshua Carter
# 8/28/2024
import calc as c

def calcMenu():
    print("\nWelcome to the calculator program.\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit\n")
    
def userChoice():
    return input("Enter a number: ")

def getUserNums():
    num1 = input("Enter a number: ")
    num2 = input("Enter a number: ")
    return num1, num2

def getUserNumsAreValid(num1 : str, num2 : str) -> bool:
    return (getUserNumIsValid(num1) and getUserNumIsValid(num2))

def getUserNumIsValid(num : str) -> bool:
    
    # Check for empty value
    if not num:
        return False

    # Check for negative sign
    absString = num
    if (num[0] == '-'):
        absString = num.split('-')[-1]
    
    digits = absString.split('.')

    # Check for non-numeric values
    for d in digits:
        if (d.isnumeric() == False): return False

    # Assume all digits are numeric
    return True

def calcDisplay(calc, num1, num2, answr):
    match calc:
        case "1":
            print(f"\n{num1} + {num2} = {answr}")
        case "2":
            print(f"\n{num1} - {num2} = {answr}")
        case "3":
            print(f"\n{num1} / {num2} = {answr}")
        case "4":
            print(f"\n{num1} * {num2} = {answr}")
        
def displayInputError():
    print("\nERROR! Please enter a valid number")

def menuRepeat():
    print("\n1. Repeat")
    print("2. Main Menu\n")
    return input("Enter a number: ")

def main():
    while True:
        # Display Menu
        calcMenu()
    
        choice = userChoice()
        if choice == "5":
            print("\nGoodbye.")
            return

        if choice in ["1", "2", "3", "4"]:
            
            repeat = True
            
            while repeat:
                match choice:
                    case "1": # Addition
                        print("\nAdd")
                    case "2": # Subtraction
                        print("\nSubtract")
                    case "3": # Division
                        print("\nDivide")
                    case "4": # Multiplication
                        print("\nMultiply")                                   
                    case "5": # End Program
                        print("\nGoodbye.")
                        return
                    case _:
                        displayInputError()

                num1, num2 = getUserNums()

                if (getUserNumsAreValid(num1,num2) == False):
                    displayInputError()
                else:
                    # Parse Input
                    num1 = float(num1)
                    num2 = float(num2)

                    # Calculation Match
                    match choice:
                        case "1": # Addition
                            answr = c.add(num1, num2)  
                        case "2": # Subtraction
                            answr = c.subtract(num1, num2)
                        case "3": # Division
                            answr = c.divide(num1, num2) 
                        case "4": # Multiplication
                            answr = c.multiply(num1, num2)

                    # Display Result of Math Operation
                    calcDisplay(choice, num1, num2, answr)

                    # Display Menu Options again
                    calcRepeat = menuRepeat()
                    if calcRepeat == "2":
                        repeat = False
        else:
            displayInputError()

if __name__ == "__main__":
    main()