import random

## global variables used in game functionality module
players = {}
points = 0
player = 0
high_score = 0


## player registration, allows for previous registered player to try to beat their previous score
def player_initials():
    player = input("Enter your initials to start or type EXT to quit: ").upper()
    for key in players:
        if key == player:
            print(player, "has a high score of", high_score,"\n")
            play_again = input("Would you like to play again as same player? ").lower()
            if play_again == "y" or play_again == "yes":
                return player
            elif play_again == "no" or play_again == "n":
                return player_initials()
            else:
                print("Please choose '(Y)es' or '(N)o'")
        else:
            continue

## reassuring player registration meets standards            
    if player == "EXT":
        print("Come back to play soon!")
        exit()
    elif len(player) > 3:
        print("Initials must be less than 3 characters.\n")
        return player_initials()
    elif len(player) <= 1:
        print("Initials must be more than 1 character.\n")
        return player_initials()
    elif player.isalpha():
        players.update({player: str(points)})
        return player
    else:
        print("Your initials must be made of letters.\n")
        return player_initials()



            
## beginner round - allows for upgrade for next round if point objective met   
def beginner():
    print("Difficulty: Beginner - For this round, each guessed word scores 5 points, each incorrect guess deducts 1 point. Good luck!\n")
    global points
    global high_score
    points = 0
    while points >= 0:
        words = ["cubicle","informant","existence","archipelago","python"]
        choice = random.choice(words)
        word = random.sample(choice, len(choice))
        word_1 = ''.join(word)
        print("Current points:", points, "\n")
        guess = input(f"Guess the word! {word_1}: ")
        if guess == choice:
            points += 5
            print("Good guess! You win 5 points!")
            high_score = points
        elif guess != choice:
            points -= 1
            print("Wrong guess, try again!")
        if points >= 15:
            next_level = input("You've scored enough points to qualify for the next round. Ready for round 2? \n").lower()
            if next_level == "yes" or next_level == "y":
                normal()
            else:
                print(f"Total Points: {points}\n")
                return
    if points < 0: 
        points = 0            
        print("You've lost all your points! Please restart game!\n")
        return
    players[player] = high_score


    
        
## normal difficulty - same as beginner with new point objective
def normal():
    print("Difficulty: Normal - For this round, each guessed word scores 6 points, each incorrect guess deducts 2 points. Good luck!\n")
    global points
    global high_score
    points = 0
    while points >= 0:
        words = ["agglomeration","metamorphosis","microscope","photosynthesis","temperature"]
        choice = random.choice(words)
        words.remove(choice)
        word = random.sample(choice, len(choice))
        word_1 = ''.join(word)
        print("Current points:", points, "\n")
        guess = input(f"Guess the word! {word_1}: ").lower()
        if guess == choice:
            points += 6
            print("6 points scored!")
            high_score = points
        else:
            points -= 2
            print("Wrong guess!\n")
        if points >= 30:
            next_level = input("You qualify for the next round. Would you like to continue? ").lower()
            if next_level == "yes" or next_level == "y":
                expert()
            else:
                print(f"Total points: {points}\n")
            return    
        if points < 0:
            points = 0
            print("You've lost all your points! Please restart game!\n")
            return
    players[player] = high_score
    
## expert difficulty - code is repeated with new point aggregates and deductions
def expert():
    print("Difficulty: Expert - For this round, each guessed word scores 7 points, each incorrect guess deducts 5 points. Think you can do it?\n")
    global points
    global high_score
    points = 0
    while points >= 0:
        words = ["microphobialism","metamorphorical","experimentalitism","arachnophobia","terantolocologist"]
        choice = random.choice(words)
        words.remove(choice)
        word = random.sample(choice, len(choice))
        word_1 = ''.join(word)
        print("Current points:", points, "\n")
        guess = input(f"Guess the word! {word_1}: ")
        if guess == choice:
            points += 7
            print("7 points scored!")
            high_score = points
        else:
            points -= 5
            print("Wrong guess!\n")
        if points < 0:
            points = 0
            print("You've lost all your points! Please restart game!")
            return        
    if points >= 50:
        print("You've hit 50 points!") ## game maxes out at 50 points - figured it would be very difficult to get here due to some words being almost impossible to figure out
        return
    players[player] = high_score
        
    
