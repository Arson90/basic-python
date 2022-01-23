# Functions
def myName(name: str):
    print(f"My name is {name}")

def validation(login: str, pin: int):
    if ((login == "Test") and (pin == 1234)):
        print("Granted access!")
    else:
        print("Access denied")

myName("Jan")
validation("Test", 1234)
validation("xyz", 1235)

def add(numA, numB):
    return numA + numB

def subtract(numA, numB):
    return numA - numB

def muliply(numA, numB):
    return numA * numB 

def divide(numA, numB):
    if numB == 0:
        return "Division by zero is undefined"
    return numA / numB

addtionResult = add(4, 10)
subtractionResult = subtract(12, 15)
multiplicationResult = muliply(4, 8)
divisionResult = divide(25, 5)
divisionResultByZero = divide(6, 0)

print(f"addtionResult = {addtionResult}")
print(f"subtractionResult = {subtractionResult}")
print(f"multiplicationResult = {multiplicationResult}")
print(f"divisionResult = {divisionResult}")
print(f"divisionResultByZero = {divisionResultByZero}")