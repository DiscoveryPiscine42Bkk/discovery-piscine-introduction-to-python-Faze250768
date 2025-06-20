num_input = input("Enter a number: ")

try:
    num = float(num_input)

    if num.is_integer():
        print("This number is not a decimal.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
