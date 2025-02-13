def binary_to_decimal(binary_str):
    """Convert a binary number (as string) to decimal."""
    return int(binary_str, 2)  

def decimal_to_binary(decimal_num):
    """Convert a decimal number to binary."""
    return bin(decimal_num)[2:]

def display_menu():
    """Display conversion options to the user."""
    print("\nChoose the following number conversion:")
    print("(1) Binary to Decimal")
    print("(2) Decimal to Binary")
    print("(3) Binary to Hexadecimal")
    print("(4) Decimal to Hexadecimal")
    print("(5) Hexadecimal to Decimal")
    print("(6) Hexadecimal to Binary")
    print("(7) Octal to Decimal")
    print("(8) Decimal to Octal")
    print("(9) Octal to Hexadecimal")
    print("(0) Exit")

def validate_binary(binary_str):
    """Check if the input is a valid binary number (only 0s and 1s)."""
    return all(char in "01" for char in binary_str)

def validate_decimal(decimal_str):
    """Check if the input is a valid decimal number (only digits 0-9)."""
    return decimal_str.isdigit()

def main():
    print("Welcome to the Number Conversion Program!")
    print("This program allows you to convert between different number systems.")

    while True:
        display_menu()
        selection = input("Selection: ").strip()

        if selection == "0":
            print("Goodbye! Thanks for using the Number Conversion Program.")
            break

        elif selection == "1":
            binary_str = input("Enter a binary number: ").strip()
            while not validate_binary(binary_str):
                print("Invalid binary number! Please enter a valid binary (only 0s and 1s).")
                binary_str = input("Enter a binary number: ").strip()
            decimal_result = binary_to_decimal(binary_str)
            print(f"{binary_str} (Binary) → {decimal_result} (Decimal)")

        elif selection == "2":
            decimal_str = input("Enter a decimal number: ").strip()
            while not validate_decimal(decimal_str):
                print("Invalid decimal number! Please enter a valid whole number (0-9).")
                decimal_str = input("Enter a decimal number: ").strip()
            decimal_num = int(decimal_str)
            binary_result = decimal_to_binary(decimal_num)
            print(f"{decimal_num} (Decimal) → {binary_result} (Binary)")

        elif selection in ["3", "4", "5", "6", "7", "8", "9"]:
            print("This option is not implemented yet! Choose another option.")

        else:
            print("Invalid choice! Please select a valid option (0-9).")

if __name__ == "__main__":
    main()
