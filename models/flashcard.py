import main_script as ms
import random as rand

def flashcard_practice(my_words):
    guess = ""
    points = 0
    attempts = 0
    while(guess != 'q'):
        word = rand.choice(list(my_words))
        d = my_words[word][1]
        pretty_print_def(d)
        guess = input("Please type the word (or q to quit): ")
        if(guess == 'q'):
            break;
        if(guess.lower() == word.lower()):
            print("Correct!")
            points += 1
            attempts += 1
        else:
            again = input("Do you want to guess again? [y/n]")
            while(again == 'y'):
                guess = input("Guess again: ")
                attempts += 1
                if(guess.lower() == word.lower()):
                    points += 1
                    print("Correct!\n")
                    break;
                again = input("Do you want to guess again? [y/n]")
            print("The word was: " + word)
    print("You got this percentage: %.2f" % (points / attempts * 100))


def pretty_print_def(s):
    s = s.replace("'", "")
    pos, part_of_speech, d = s[1:-1].split(':', 2)
    part_of_speech, junk = part_of_speech.split(",")
    part_of_speech = part_of_speech[1:]
    d = d[1:]
    print("%20s %-s " % ("Part of Speech: ", part_of_speech))
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