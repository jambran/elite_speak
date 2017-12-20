
import random as rand

def flashcard_practice(my_words):
    # initialize variables to keep track of correct guesses, attempts, and user's guess
    guess = ""
    points = 0
    attempts = 0
    if(not my_words): #if the dictionary is empty
        print("You don't have any words to practice yet.")
        return
    # user may enter q to quit
    while(guess != 'q'):
        # choose a word from personal dictionary
        word = rand.choice(list(my_words))
        #show the definition, not the word
        pretty_print_def(my_words[word])
        guess = input("Please type the word (or q to quit): ")
        if(guess == 'q'):
            break
        if(guess.lower() == word.lower()): # if correct...
            print("Correct!")
            points += 1
            attempts += 1
        else: # if incorrect...
            attempts += 1
            again = input("Do you want to guess again? [y/n]")
            while(again == 'y'):
                guess = input("Guess again: ")
                attempts += 1
                if(guess.lower() == word.lower()):
                    points += 1
                    print("Correct!\n\n")
                    break
                again = input("Do you want to guess again? [y/n]  ")
            print("The word was: " + word + "\n")
    try:
        print("You got this percentage: %.2f" % (points / attempts * 100))
    except ZeroDivisionError:
        print("\nYou got this percentage: 0.00%")


def pretty_print_def(tple):
    # tple is a tuple from the my_words dictionary
    # has form (num_times_defined, definition, last_time_defined, POS)
    d = tple[1]
    print("%20s %-s " % ("Part of Speech: ", tple[3]))
    # do this to word-wrap
    if (len(d) < 50):
        print("%20s %s" % ("Definition: ", d))
    else:
        print("%20s %s-" % ("Definition: ", d[:50]))
        d = d[50:]
        while (len(d) > 50):
            print("%20s %s-" % ("", d[:50]))
            d = d[50:]
        print("%20s %s" % ("", d))
    print("\n")
