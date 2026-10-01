# Made by Arihaan Yadav.
# Simpl Project: Calculator app.
# Knowledge needed: Data types(mostly (str)ing and (float), Taking user input, Functions(defining functions and print() functions), 
# Condtionals, Loops(while), try:, except:, and break.
# Best for beginner projects :)

# Start 
def calculator():

    # Checking first number
    while True:
        try:
            first_num = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid!")

    # Checking operation
    while True:
        operation = input("Enter operation. Choose from (a)ddition, (s)ubtraction, (m)ultipication, and (d)ivision: ").lower()
        if operation != "s" and operation != "a" and operation != "s" and operation != "d":
            print("Invalid!")
        else:
            break

    # Checking second number
    while True:
        try:
            second_num = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid!")
    
    # Logic for calculator
    if operation == "a":
        print(f"Answer: {first_num + second_num}")
    elif operation == "s":
        print(f"Answer: {first_num - second_num}")
    elif operation == "m":
        print(f"Answer: {first_num * second_num}")
    elif operation == "d":
        print(f"Answer: {first_num / second_num}")
    else:
        pass

print("------------------------------------")
print("-------------CALCULATOR-------------")
print("------------------------------------")

# Calling function
calculator()

# End: Thank You!