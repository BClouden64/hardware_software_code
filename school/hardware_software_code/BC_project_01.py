def main():
    print("Hello, I would like to get to know a little about you.")
    print("Please answer a few brief questions.")

    name = "Brandon"
    college = "Guttman CC"
    high_school = "Tiegerman High School"
    more_fun = college

    print(f"What is your name?{name}")
    print(f"{name}, What college are you attending?{college}")
    print(f"{name}, What high school did you attend?{high_school}")
    print(f"{name}, Which institution is more fun?{more_fun}")

    print(f"\nIt was nice to speak with you, {name}")
    print(f"You are currently attending, {college}")
    print(f"I learned that your high school's name is {high_school}")
    print(f"You think {college} is more fun than {high_school}")
    print("It was fun getting to know a little about you.")
    print("Let's do this again!")

if __name__ == "__main__":
    main()
