from levels_pkg import levels

## intro to game
print("Get ready for WORD SHUFFLE!\n")

## main menu
def word_search():
        name = levels.player_initials()

        print(f"Welcome {name}!")
        print("")
        print("Choose your level to begin: ")
        print("1) -- Beginner --")
        print("2) -- Intermediate --")
        print("3) -- Expert --")
        print("")

word_search()

## game loop with appropriate exit
while True:
    level_choice = input("Choose wisely! ").lower()
    if level_choice == "1":
        levels.beginner()
        word_search()
    elif level_choice == "2":
        levels.normal()
        word_search()
    elif level_choice == "3":
        levels.expert()
        word_search()
    elif level_choice == "q":
        print("See you next time!")
        break
    else:
        print("Choose valid option! -- or enter Q if you'd like to exit.")