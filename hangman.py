# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    word_len=len(secret_word)
    count=0
    for guess in letters_guessed:
        for letter in secret_word:
            # if guess == ' ' or guess == '_':#looking for spacing not sure if needed
            #     break
            if guess == letter:
                count+=1
    if count == word_len:
        return True
    else:
        return False
# testing for is_word_guessed function. came back good when first tested.
# test_is_word_guessed = (('test', ['a','b','c','d','e']),('letter','abcdefghijklmnopqrstuvwxyz'),('albequrqe','abcdefghijklmnopqrstuvwxyz'),('people','lol'),('test','abcdefghijklmno'))
# for word,letters in test_is_word_guessed:
#     print(is_word_guessed(word,letters))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word=""
    #print(guessed_word)
    for letter in secret_word:
        for guess in letters_guessed:
            if letter == guess:
                guessed_word+=letter
        if letters_guessed.count(letter)==0:
            guessed_word+='_ '
    return guessed_word
#testing function get_guessed_word. worked fine on first run
# test_get_guessed_word = (('healhty', ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']),
#                          ('letter',['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']),
#                          ('wisconsin',['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']),
#                          ('yellow',['e','f','g','h','i','j','k','l','m','n','o','p']),
#                          ('bananas',['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
# for word,letters in test_get_guessed_word:
#     print(get_guessed_word(word,letters))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    unused_letters=""
    for letter in alphabet:
        if letters_guessed.count(letter)==0:
            unused_letters+=letter
    return unused_letters
#testing function get_available_letters(). worked fine when tested.
# test_get_available_letters = (['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['a','b','c','d','e','j','k','l','m','n','o'],['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'])
# for test_list in test_get_available_letters:
#     print(get_available_letters(test_list))

def is_letter_in_word(secret_word,user_guess):
    '''
    checks to see if users guess is in word
    returns true if it is in the word
    otherwise returns false
    '''
    if user_guess in secret_word:
        return True
    else:
        return False

def punishment(warnings,guesses):
    '''
    handles deducting points from warnings and guesses
    #not sure i will actually use this will think about it
    '''
    if warnings > 0:
        warnings -= 1
        # do you need to print saying they lost a warning or a guess?
    else:
        guesses -= 1
    return (warnings,guesses)

def unique_letters(secret_word):
    '''
    used to help calculate the total score when the player wins
    '''
    alphabet=string.ascii_lowercase
    count_of_letters=[]
    for letter in alphabet:
        if secret_word.count(letter)>0:
            count_of_letters.append(secret_word.count(letter))
    return len(count_of_letters)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    user_guess=""
    guessed_word=""
    letters_guessed_so_far = ""
    consonants="bcdfghjklmnpqrstvwxyz"
    vowels="aeiou"
    available=get_available_letters(letters_guessed_so_far)
    word_len=len(secret_word)
    guesses_remain=6
    warning_remain=3
    point=0
    while True:
        if guesses_remain>0:
            if guesses_remain==6 and warning_remain==3:
                print("Welcome to Hangman the Game!")
                print("The word i am thinking of is %d"%(word_len),"characters long.")
            print("------------------------------------")
            print("Number of Guesses left: %d"%(guesses_remain))
            print("Available Letters: %s"%(available))
            guess=input("Enter your guess here: ")
            if str.isalpha(guess)==True:
                #if its a letter
                user_guess = str.lower(guess)
                #make sure its lower case
                if user_guess in available:
                    letters_guessed_so_far+=user_guess
                    #do something with the user_guess
                    if is_letter_in_word(secret_word,user_guess)==True:
                        print("That is in the word.")
                    else:
                        #not in the secret word, is it a vowel or a consonant?
                        print("Thats not in the word. Try again.")
                        if user_guess in consonants:
                            guesses_remain -= 1
                        elif user_guess in vowels:
                            guesses_remain -= 2
                else:
                    # the letter has been used before deduct points
                    print("You have used this guess before")
                    if warning_remain > 0:
                        warning_remain -= 1
                        # do you need to print saying they lost a warning or a guess?
                    else:
                        guesses_remain -= 1
                available = get_available_letters(letters_guessed_so_far)
                guessed_word=get_guessed_word(secret_word,letters_guessed_so_far)
                print("Guess so Far: ", guessed_word)
            elif str.isalpha(guess)==False:
                #not a valid entry
                print("Your entry is invalid please try again")
                if warning_remain > 0:
                    warning_remain-=1
                    #do you need to print saying they lost a warning or a guess?
                else:
                    guesses_remain-=1
        else:
            #print game over, print what the secret word is
            print("No No No that is not the magic password. You lose.")
            print("The correct word is:",secret_word)
            break
        if is_word_guessed(secret_word, letters_guessed_so_far) == True:
            print("Congratualations You Win!")
            # function to calculate total points
            point = guesses_remain * unique_letters(secret_word)
            print("Your number of points earned for this game are: %d" % (point))
            break


    # # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
#testing words before implementing random function below
# testing_words = ["england","test","unibrow","roman","qualified"]
# for test_word in testing_words:
#     hangman(test_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
