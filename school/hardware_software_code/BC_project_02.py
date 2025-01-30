def introduction():
    """Prints the introduction message for the program."""
    print("Welcome to my conversation program")
    print("I will keep asking questions until you type 'exit'.\n")

def ask_questions():
    """Runs the loop to ask questions until the user types 'exit'."""
    questions_and_answers = {
        "What is your name? ": "Brandon",
        "What is your favorite show, {name}? ": "Breaking Bad",
        "Do you like programming, {name}? ": "Yes",
        "What is your favorite sport, {name}? ": "Soccer"
    }

    count = 0
    user_name = input("1. " + list(questions_and_answers.keys())[0]).strip()

    if user_name.lower() == "exit":
        print("\nToo bad you did not want to chat! Maybe next time!")
        print("You answered no questions")
        return

    print(f"{user_name}")

    for i, (question, answer) in enumerate(list(questions_and_answers.items())[1:], start=2):
        response = input(f"{i}. {question.format(name=user_name)}").strip().lower()
        print(answer) 
        if response == "exit":
            break
        count += 1

    print(f"\nThanks for chatting with me, {user_name}")
    print(f"You answered {count} questions")

def main():
    introduction()
    ask_questions()

if __name__ == "__main__":
    main()
