# main.py

from app.calculator import Calculator

def main():
    calc = Calculator()
    print("Welcome to the Calculator REPL.")
    print("Type 'help' for instructions or 'exit' to quit.")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        elif user_input.lower() == 'help':
            print("""
Available commands:
    add <number1> <number2>        - Add two numbers
    subtract <number1> <number2>   - Subtract second number from first
    multiply <number1> <number2>   - Multiply two numbers
    divide <number1> <number2>     - Divide first number by second
    help                           - Show this help message
    exit or quit                   - Exit the REPL

Examples:
    add 2 3
    subtract 10 4
    multiply 5 6
    divide 8 2
""")
            continue

        # Split the input into parts
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid command. Type 'help' for instructions.")
            continue

        command, num1_str, num2_str = parts

        # Convert strings to numbers
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            print("Invalid numbers. Please enter numeric values.")
            continue

        # Perform the operation
        try:
            if command.lower() == 'add':
                result = calc.add(num1, num2)
            elif command.lower() == 'subtract':
                result = calc.subtract(num1, num2)
            elif command.lower() == 'multiply':
                result = calc.multiply(num1, num2)
            elif command.lower() == 'divide':
                result = calc.divide(num1, num2)
            else:
                print(f"Unknown command '{command}'. Type 'help' for instructions.")
                continue
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
