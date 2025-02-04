def greetings():
    print("Give me two numbers and I will tell you the largest number!")

def get_largest(largest, value):
    if largest is None:
        return value
    elif value > largest:
        return value
    return largest

def main():
    stop_loop = "no"
    greetings()
    largest = None

    while stop_loop != "yes":
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            largest = get_largest(largest, num1)
            largest = get_largest(largest, num2)

            print("The largest value so far is {}".format(largest))

        except ValueError:
            print("Invalid input! Please enter an integer.")

        stop_loop = input("Type 'yes' to exit program (or press Enter to continue): ").lower().strip()

if __name__ == "__main__":
    main()
