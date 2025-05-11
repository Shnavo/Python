# first_number = float(input("Provide first number: "))
# second_number = float(input("Provide second number: "))
# operation = input("Type in the number of operation you want to use: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n")

# if operation == "1":
#     result = first_number + second_number
#     result_int = int(result)
#     if result == result_int:
#         print(result_int)
#     else:
#         print(result)
# elif operation == "2":
#     result = first_number - second_number
#     result_int = int(result)
#     if result == result_int:
#         print(result_int)
#     else:
#         print(result)
# elif operation == "3":
#     result = first_number * second_number
#     result_int = int(result)
#     if result == result_int:
#         print(result_int)
#     else:
#         print(result)
# elif operation == "4":
#     if second_number != 0:
#         result = first_number / second_number
#         result_int = int(result)
#         if result == result_int:
#             print(result_int)
#         else:
#             print(result)
#     else:
#         print("You can't divide by zero")

    
# 1. Napisz funkcję która przyjmie 3 parametry: 1. liczba, 2. liczba i operator i wypisze wynik działania
# 2. Przerób if elify na match case'a !!DONE!!
# 3. Napisz 4 funkcje, po jednym dla każdego działania, które będą przyjmować 2 liczby i zwracać wynik !!HALF-DONE!!
# 4. kolejna funkcja której zadaniem jest przyjąć na wejściu liczbę i sprawdzić czy to liczba całkowita, czy ma wartość po przecinku !!DONE!!
# na podstawie tego (^) printować odpowiednią formę wyniku !!DONE!!
# DODATEK jak zastosować while'a żeby sprawdzać czy user faktycznie podał liczbę oraz operator i jeśli nie podał, prosić go do skutku podawać !!DONE!!

 # while first_number not in numbers: #not correct, mają być liczby nie cyfry
    #     first_number = int(input("Didn't provide a number. Please provide first number: "))

# 1. Ma działać na floatach
# Tips:
# 1.1 Funkcja do parse'owania floatów
# User może podać kropkę albo przecinek jako decimal separator
# Jako error uwzględnij sytuacje w których: jest kropka na początku; na końcu; więcej niż jedna kropka; 
# Kropka i przecinek może istnieć tylko jeśli znajduje się MIĘDZY dwoma cyframi

# region Operations
def addition(first_number, second_number):
    return first_number + second_number

def substraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number
#endregion

def number_checker(input):
    numbers = [str(number) for number in range(10)]
    for symbol in input:
        if symbol in numbers or symbol == ".": # added here
            continue
        else:
            return False
    else:
        return True
    
def period_checker(input): # added here
    i = 0
    period = False
    for symbol in input:
        i += 1
        if i == 1 and symbol == ".":
            return False
        elif i == len(input) and symbol == ".":
            return False
        elif symbol == ".":
            if not period:
                period = True
            else:
                return False       
    else:
        if period: # better practice than period == True
            return True
        else:
            return None

def float_checker(result):
    result_int = int(result)
    if result == result_int:
        return result_int
    else:
        return round(result, 10)

def calculator():    
    operators = ["+", "-", "*", "/"]
    
    first_number = input("Please provide first number: ")
    # print(period_checker(first_number))
    while not number_checker(first_number):
        first_number = input("Didn't provide a number. Please provide a first number: ")
    while period_checker(first_number) == False: # added here
        first_number = input(f"There seems to be an error with the periods. Please check the periods {first_number} and correct any mistakes: ")

    operator = input("Provide a symbol of operation you would like to make from this list: +, -, *, /: ")
    while operator not in operators:
        operator = input("Not a correct operator. Provide a symbol from this list: +, -, *, /: ")

    second_number = (input("Please provide second number: "))
    if operator == "/":
        while not number_checker(second_number) or second_number == "0" or period_checker(second_number) == False:
            if second_number == "0":
                second_number = input("Can't divide by zero. Please provide a second number: ")
            elif not number_checker(second_number):
                second_number = input("Didn't provide a number. Please provide a second number: ")
            else:
                second_number = input(f"There seems to be an error with the periods. Please check the periods {second_number} and correct any mistakes: ")
        
    else:
        while not number_checker(second_number):
            second_number = input("Didn't provide a number. Please provide a second number: ")
        while period_checker(second_number) == False: # added here
            second_number = input(f"There seems to be an error with the periods. Please check the periods {second_number} and correct any mistakes: ")

#region ADDED THIS SECTION
    if period_checker(first_number) is None and period_checker(second_number) == None:
        first_number = int(first_number)
        second_number = int(second_number)
    elif period_checker(first_number) and period_checker(second_number) == None:
        first_number = float(first_number)
        second_number = int(second_number)
    elif period_checker(first_number) is None and period_checker(second_number):
        first_number = int(first_number)
        second_number = float(second_number)
    else:
        first_number = float(first_number)
        second_number = float(second_number)
#endregion
    match operator:
        case "+":
            result = addition(first_number, second_number)
        case "-":
            result = substraction(first_number, second_number)
        case "*":
            result = multiplication(first_number, second_number)
        case "/":
            result = division(first_number, second_number)

    print(float_checker(result))
    

if __name__ == "__main__":
    repeat = "Y"
    while repeat.upper() == "Y":
        calculator()
        repeat = input("Do you want to use the calculator again? Y/N: ")
        # if repeat.upper() == "Y" or repeat.upper() == "N":
        while repeat.upper() not in ["Y", "N"]:
            repeat = input("Please provide one of these as an answer Y/N: ")
        