# Function definitions

def addition(*args):
    """Function to perform addition."""
    return sum(args)

def subtraction(a, b):
    """Function to perform subtraction."""
    return a - b

def multiplication(*args):
    """Function to perform multiplication."""
    result = 1
    for arg in args:
        result *= arg
    return result

def division(a, b):
    """Function to perform division."""
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

# Calculator operations
print("Welcome to the Calculator!")

while True:
    print("\nOperation Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Select operation (1-2-3-4-5): ")

    if choice == '5':
        print("Exiting the calculator...")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please try again.")
        continue

    try:
        numbers = input("Enter numbers for the operation separated by spaces: ")
        numbers = list(map(float, numbers.split()))

        if choice == '1':
            print("Sum:", addition(*numbers))
        elif choice == '2':
            print("Difference:", subtraction(numbers[0], numbers[1]))
        elif choice == '3':
            print("Product:", multiplication(*numbers))
        elif choice == '4':
            print("Quotient:", division(numbers[0], numbers[1]))

    except ValueError:
        print("Invalid number input. Please try again.")
    except IndexError:
        print("Not enough numbers provided for the operation. Please try again.")
    except Exception as e:
        print("An error occurred:", e)
