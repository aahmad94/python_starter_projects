import random
while True:

    print(""" 
▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█
▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄
▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█
▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█
▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█
▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█
▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█
▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█
▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█

Guess what number I'm thinking of!""")
    # generate a random number between 1 and 10
    range_lower = 1
    range_upper = int(input("""
SELECT DIFFICULTY:

YOU HAVE 5 GUESSES TO GUESS THE NUMBER I'M THINKING:

EASY - MY NUMBER WILL BE BETWEEN 1 AND 10; TYPE '10'
MEDIUM - MY NUMBER WILL BE BETWEEN 1 AND 5; TYPE '50'
HARD - MY NUMBER WILL BE BETWEEN 1 AND 100; TYPE '100': """))

    N = random.randint(range_lower, range_upper)

    # generate list of guesses; use it to limit the number of while loops to
    guesses = []
    while len(guesses) < 5:

        # get a number guess from the player
        try:
            player_input = input("\nPick a number between " + str(range_lower) + " and " + str(range_upper) + " : ")
            guess = int(player_input)
        except NameError:
            print("{} isn't a number!".format(player_input))
        else:
            # compare guess to secret number
            # respond hit/miss
            if guess < N:
                print("That's too low.")
            elif guess > N:
                print("That's too high.")
            else:
                if guess == N:
                    print("""
░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
░░░░█░░░░░░░░░░░░░█░░░░
░░░█░░░░░░░░░░▄▄▄░░█░░░
░░░█░░▄▄▄░░▄░░███░░█░░░
░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
░░░█░░▀█▀█▀█▀█▀█▀░░█░░░
░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░ 

That's the number!""")
                break
            # add guess to list of guesses
            guesses.append(guess)


    try:
        play_again = input("\nWould you like to play again? ('yes'/'no'): ")
    except TypeError:
        print("That's not one of the options. Enter 'yes' if you would like to play again or 'no' to exit.")
    if play_again == 'yes':
        continue
    elif play_again == 'no':
        print("\nGAME OVER!")
        break
