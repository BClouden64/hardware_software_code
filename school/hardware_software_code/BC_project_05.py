def main():
    print("This program adds two whole numbers.")
    print("You can enter numbers repeatedly until you choose to exit.\n")

    while True:

        while True:
            first_number = input("Enter first number: ")
            if first_number.isdigit():
                first_number = int(first_number)
                print(f"{first_number} is a good number")
                break
            else:
                print("Invalid Number, Try again!!!")


        while True:
            second_number = input("Enter second number: ")
            if second_number.isdigit():
                second_number = int(second_number)
                print(f"{second_number} is a good number")
                break
            else:
                print("Invalid Number, Try again!!!")

        result = first_number + second_number
        print("\nLet's do some adding!")
        print(f"{first_number} + {second_number} = {result}\n")

        exit_choice = input("Type 'yes' to end program or press Enter to continue: ").strip().lower()
        if exit_choice == "yes":
            print("Goodbye!!!\nCome back when you have more numbers :)")
            break

if __name__ == "__main__":
    main()
