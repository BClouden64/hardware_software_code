def display_menu():
    menu_dict = {
        '1': 'apples',
        '2': 'bananas',
        '3': 'cherries',
        '4': 'grapes'
    }
    print("Pick your favorite fruit")
    for items, values in menu_dict.items():
        print("\t{}. {}".format(items, values))

    choice = input("Choose an option: ").strip()
    choices = list(menu_dict.keys())

    if choice in choices:
        return menu_dict[choice]
    else:
        print("Invalid Selection\nTry Again:")
        return display_menu()

def main():
    fruit = display_menu()
    print("Wow, I like {} too!".format(fruit))

if __name__ == "__main__":
    main()
