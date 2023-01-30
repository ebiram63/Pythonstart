import random 

attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("there is currently no high score, it is your for the taking!")
    else:
        print("the current high score is {} attempts" . format(min(attempts_list)))

def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guessing")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) " . format(player_name))
    #where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "Yes":
        try:
            guess = input("pick a number between 1 to 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number between 1 to 10")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts" . format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No)")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That is cool, have a good one!")
                    break
                elif int(guess) > random_number:
                    print("It is lower")
                    attempts += 1
            elif int(guess) < random_number:
                print("It is higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value.Try again...")
            print("({})". format(err))
    else:
        print("That is cool, have a good one!")

if __name__ == "__main__":
    start_game()