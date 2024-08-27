# CTS 285
# M1HW
# Max Cayton, Joshua Carter
# 8/27/2024

# Calculation Functions Bronze

import calc as c

def calcMenu():
    
    print()
    print("Welcome to the calculator program.")
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    print()
    

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
    
    if calc == "1":
        print()
        print(f"{num1} + {num2} = {answr}")
        
    elif calc == "2":
        print()
        print(f"{num1} - {num2} = {answr}")
        
    elif calc == "3":
        print()
        print(f"{num1} / {num2} = {answr}")
        
    elif calc == "4":
        print()
        print(f"{num1} * {num2} = {answr}")
        
def displayInputError():
    print()
    print("ERROR! Please enter a valid number")

def menuRepeat():
    
    print()
    print("1. Repeat")
    print("2. Main Menu")
    print()
    return input("Enter a number: ")

def main():
    
    while True:
        
        calcMenu()
        
        choice = userChoice()

        if choice == "5":
            
            print()
            print("Goodbye.")
            return

        if choice in ["1", "2", "3", "4"]:
            
            repeat = True
            
            while repeat:
                
                if choice == "1":
                    
                    print()
                    print("Add")
                    
                elif choice == "2":
                    
                    print()
                    print("Subtract")
                    
                elif choice == "3":
                    
                    print()
                    print("Divide")
                    
                elif choice == "4":
                    
                    print()
                    print("Multiply")

                num1, num2 = getUserNums()

                if (getUserNumsAreValid(num1,num2) == False):
                    displayInputError()
                else:
                    # Parse Input
                    num1 = float(num1)
                    num2 = float(num2)

                    if choice == "1":
                        answr = c.add(num1, num2)                        
                    elif choice == "2":                        
                        answr = c.subtract(num1, num2)                        
                    elif choice == "3":                        
                        answr = c.divide(num1, num2)                        
                    elif choice == "4":                        
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


