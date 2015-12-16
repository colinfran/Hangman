"""
    Name: Colin Franceschini
    Description: This program creates a hangman game. It imports a list of
                 words from the file inputed by the user. A random word is
                 selected from the list of words and is used as the hangman
                 word. The user then guesses letters to try to figure out
                 the hangman word. The hangman word is represented by a row
                 of underscores. If the user guesses a letter that does occur
                 in the word, that letter is revealed in its correct positions.
                 If the guessed letter does not occur in the word, the game
                 draws one element of a hanged man stick figure. The user can
                 only guess 6 incorrect letters or the user will lose.
"""

from graphics import *
from sys import *
from hangman_support import *


def read_input_file(file_name):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)

    Returns: the text in the file as a large, possibly multi-line, string
    """
    infile = open(file_name, "r")  # open file for reading
    filetext = infile.read().splitlines()  # reads content, splits into lines
    infile.close()  # closes the file
    return filetext  # returns the text of the file, as a single string


def valid_word(hangmanfile):
    """
    Checks to see if the words in the word list is are usable words. If the
    words are usable, they are appended to a new list.

    Parameter: the text in the file as a large, possibly multi-line, string

    Returns: the new list of usable words
    """
    word_check = []
    for word in hangmanfile:
        if word.isalpha():
            word_check.append(word)
    return word_check


def valid_letter(letters_guessed, guess_letter, letters_guessed_incorrect):
    """
    Checks to see if the letter entered is a valid letter. If it is a valid
    letter, it returns True. If the next letter inputed is the same letter as
    the previous inputed letter, it returns an error message. If the letter
    inputed is more than one letter, it returns an error message. If the letter
    inputed is not an alphabetical character, it returns an error message. If
    the user did not enter anything, it returns an error message.

    Parameters: letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                guess_letter = The user inputed letter
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the hangman
                                            word

    Returns: True - if the letter entered by the user is a valid letter
            and is a letter.
            Returns - false if the inputed letter is the same as the previous
            letter, if the inputed letter is more than one letter, if it is not
            alphabetical character, and if the user did not enter anything
    """
    var = False
    for i in range(len(letters_guessed)):
        if letters_guessed[i] == guess_letter:
            var = True
    for j in range(len(letters_guessed_incorrect)):
        if letters_guessed_incorrect[j] == guess_letter:
            var = True
    if guess_letter == '':
        print("Error. Please enter a letter")
        return False
    elif len(guess_letter) > 1:
        print("Error. Please enter only one letter")
        return False
    elif var:
        print("Error. Please enter a letter that hasn't been entered")
        return False
    elif guess_letter.isalpha() is not True:
        print("Error. Please enter a valid letter")
    return True


def check_letter(letters_guessed, pick_word, guess_letter, check_valid,
                 letters_guessed_incorrect, valid_pattern, word_check):
    """
    Checks to see if the inputed letter is in the hangman word. If it is in
    the hangman word, the letter is appended to the index list. If it
    is not in the hangman word, the letter is appended to the
    letters_guessed_incorrect list.

    Parameters: letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                pick_word = tbe word from the list that was picked by
                            the function provided in hangman_support.py
                guess_letter = The user inputed letter
                check_valid = the valid letter entered by the user
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the
                                            hangman  word
                valid_pattern =  a list of words in the word list that match
                                 the same length as the hangman word and whose
                                 letter match the pattern of the currently
                                 revealed word and the list of incorrect
                                 guesses
                word_check = a list of usable words that can be used in the
                             hangman game
    """
    valid = []
    if guess_letter in pick_word and guess_letter.isalpha():
        indexes = []
        for i in range(len(pick_word)):
            if guess_letter == pick_word[i]:
                letters_guessed[i] = guess_letter
                indexes.append(i)
        for word in valid_pattern:
            keep = True
            for i in indexes:
                if word[i] != guess_letter:
                    keep = False
                    break
            if keep:
                valid.append(word)
    else:
        if guess_letter.isalpha():
            letters_guessed_incorrect.append(guess_letter)
        for word in valid_pattern:
            if not guess_letter in word:
                valid.append(word)
    return valid


def draw_platform(window, WINSIZE):
    """
    Draws the platform for the hangman game in the graphics window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE)
    second_point = Point(WINSIZE * (3/4), WINSIZE)
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)
    third_point = Point(WINSIZE * (1/2), WINSIZE * (1/10))
    fourth_point = Point(WINSIZE * (1/2), WINSIZE)
    line = Line(third_point, fourth_point)
    line.setWidth(6)
    line.draw(window)
    fifth_point = Point(WINSIZE * (1/4), WINSIZE * (1/10))
    sixth_point = Point(WINSIZE * (1/2), WINSIZE * (1/10))
    line = Line(fifth_point, sixth_point)
    line.setWidth(6)
    line.draw(window)
    seventh_point = Point(WINSIZE * (1/4), WINSIZE * (1/10))
    eigth_point = Point(WINSIZE * (1/4), WINSIZE * (3.5/20))
    line = Line(seventh_point, eigth_point)
    line.setWidth(6)
    line.draw(window)


def draw_head(window, WINSIZE):
    """
    Draws the head of the hangman for the hangman game in the graphics window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    center = Point(WINSIZE * (1/4), WINSIZE * (3/10))
    radius = WINSIZE * (5/40)
    circle = Circle(center, radius)
    circle.setWidth(6)
    circle.draw(window)


def draw_body(window, WINSIZE):
    """
    Draws the body of the hangman for the hangman game in the graphics window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE * (17/40))
    second_point = Point(WINSIZE * (1/4), WINSIZE * (7/10))
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)


def draw_left_arm(window, WINSIZE):
    """
    Draws the left arm of the hangman for the hangman game in the graphics
    window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE * (3/5))
    second_point = Point(WINSIZE * (1/8), WINSIZE * (2/5))
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)


def draw_right_arm(window, WINSIZE):
    """
    Draws the right arm of the hangman for the hangman game in the graphics
    window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE * (3/5))
    second_point = Point(WINSIZE * (3/8), WINSIZE * (2/5))
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)


def draw_left_leg(window, WINSIZE):
    """
    Draws the left leg of the hangman for the hangman game in the graphics
    window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE * (7/10))
    second_point = Point(WINSIZE * (1/8), WINSIZE * (9/10))
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)


def draw_right_leg(window, WINSIZE):
    """
    Draws the right leg of the hangman for the hangman game in the graphics
    window

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    first_point = Point(WINSIZE * (1/4), WINSIZE * (7/10))
    second_point = Point(WINSIZE * (3/8), WINSIZE * (9/10))
    line = Line(first_point, second_point)
    line.setWidth(6)
    line.draw(window)


def draw_frown_eyes(window, WINSIZE):
    """
    Draws the eyes of the hangman for the hangman game in the graphics window
    when the user loses

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    center = Point((WINSIZE * (1/4)) - (WINSIZE * 1/30),
                   ((WINSIZE * (3/10)) - (WINSIZE * 1/30)))
    radius = WINSIZE * (1/50)
    circle = Circle(center, radius)
    circle.setFill("black")
    circle.draw(window)
    center = Point((WINSIZE * (1/4)) + (WINSIZE * 1/30),
                   ((WINSIZE * (3/10)) - (WINSIZE * 1/30)))
    circle = Circle(center, radius)
    circle.setFill("black")
    circle.draw(window)


def draw_frown_mouth(window, WINSIZE):
    """
    Draws the mouth of the hangman for the hangman game in the graphics window
    when the user loses. Was made by two circles. The white circle covers
    the black circle to make a frown.

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    # the frown was drawn using two circles, one black and the other white.
    # because the lower circle is white and the background is white, the
    # frown shape is created
    center = Point(WINSIZE * (1/4), WINSIZE * (14/40))
    radius = WINSIZE * (1/25)
    circle = Circle(center, radius)
    circle.setFill("black")
    circle.draw(window)
    center = Point(WINSIZE * (1/4), WINSIZE * (15/40))
    circle = Circle(center, radius)
    circle.setOutline("white")
    circle.setFill("white")
    circle.draw(window)


def draw_lose_text(window, WINSIZE):
    """
    Creates a text box in the graphics window when the user loses

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
    """
    Text(Point(WINSIZE * (3/4), WINSIZE * (1/2)),
         'YOU LOSE! \n click the window to exit').draw(window)


def draw_everything(window, WINSIZE, letters_guessed_incorrect):
    """
    This function calls the drawing functions each time the user runs out
    of a guess.

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the
                                            hangman word
    """
    if len(letters_guessed_incorrect) == 1:
        draw1 = draw_head(window, WINSIZE)
    if len(letters_guessed_incorrect) == 2:
        draw2 = draw_body(window, WINSIZE)
    if len(letters_guessed_incorrect) == 3:
        draw3 = draw_left_arm(window, WINSIZE)
    if len(letters_guessed_incorrect) == 4:
        draw4 = draw_right_arm(window, WINSIZE)
    if len(letters_guessed_incorrect) == 5:
        draw5 = draw_left_leg(window, WINSIZE)
    if len(letters_guessed_incorrect) == 6:
        draw6 = draw_right_leg(window, WINSIZE)
        draw7 = draw_frown_eyes(window, WINSIZE)
        draw8 = draw_frown_mouth(window, WINSIZE)
        draw9 = draw_lose_text(window, WINSIZE)


def hangman_1(word_check, letters_guessed, letters_guessed_incorrect):
    """
    After the user agrees to play the game, this function creates a graphics
    window called project Project 3: Hangman. It then draws the platform of the
    hangman game. Then, a word is randomly chosen from the word list using the
    function provided in the hangman_support.py file. That word is then split
    into a list of letters. Displaying in the text window, the word is
    represented by a row of underscores. The text window then displays the
    number of words in the word list match the same pattern as the the
    underscores and correct letters guessed. It then continues to the
    hangman_2 function.

    Parameters: word_check = a list of usable words that can be used in the
                             hangman game
                valid_pattern =  a list of words in the word list that match
                                 the same length as the hangman word and whose
                                 letter match the pattern of the currently
                                 revealed word and the list of incorrect
                                 guesses
                letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the hangman
                                            word
    """
    window = GraphWin("Project 3: Hangman", WINSIZE, WINSIZE)
    draw0 = draw_platform(window, WINSIZE)  # draws starting hangman platform
    # this function (which is provided for us in hangman_support.py) picks a
    # random word from the word list to be used as the hangman word
    pick_word = choose_word(word_check)
    pick_word = list(pick_word.upper())
    print("\n")
    print("_ " * len(pick_word))
    valid_pattern = []
    for i in range(len(word_check)):
        if len(pick_word) == len(word_check[i]):
            valid_pattern.append(word_check[i].upper())
    print()
    print(len(valid_pattern),
          "words in the words list match the above pattern")
    for i in range(len(pick_word)):
    # this prints out underscores that represent each letter of the word
        letters_guessed.append("_ ")
    play_hangman_2 = hangman_2(letters_guessed_incorrect, window, WINSIZE,
                               pick_word, valid_pattern, letters_guessed,
                               word_check)


def hangman_2(letters_guessed_incorrect, window, WINSIZE, pick_word,
              valid_pattern, letters_guessed, word_check):
    """
    This function continues from the playhangman_1 function. It asks the user
    to guess a letter. It then checks to see if the letter is a valid letter
    that could be inputed. If it is, it checks to see if the letter is in the
    hangman word. It then continues to hangman_3. After hangman_3 finishes, it
    it then continues to hangman_4.

    Parameters: letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the hangman
                                            word
                window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
                pick_word = tbe word from the list that was picked by
                            the function provided in hangman_support.py
                valid_pattern =  a list of words in the word list that match
                                 the same length as the hangman word and whose
                                 letter match the pattern of the currently
                                 revealed word and the list of incorrect
                                 guesses
                letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                word_check = a list of usable words that can be used in the
                             hangman game
    """
    while True:
        print("\n")
        guess_letter = input('Guess a letter: ').upper()
        print("\n")
        # checks if the letter is a valid letter that can be used to play
        check_valid = valid_letter(letters_guessed, guess_letter,
                                   letters_guessed_incorrect)
        if not check_valid:
            continue
        # This next function checks to see how many words match the pattern
        # of the underscores and correctly guessed letters. It also adds
        # the letters to that are incorrectly guessed and the letters that
        # were correctly guessed to their appropriate list
        valid_pattern = check_letter(letters_guessed, pick_word, guess_letter,
                                     check_valid, letters_guessed_incorrect,
                                     valid_pattern, word_check)
        # This next function will draw its appropriate item every time a
        # letter is guessesd incorrectly
        draw_everything1 = draw_everything(window, WINSIZE,
                                           letters_guessed_incorrect)
        print()
        play_hangman_3 = hangman_3(pick_word, letters_guessed,
                                   letters_guessed_incorrect)
        if letters_guessed == pick_word or len(letters_guessed_incorrect) >= 6:
            break
        print()
        # this prints the number of words in the word list that exactly match
        # the pattern of the currently revealed word while also not containing
        # incorrect guesses
        print(len(valid_pattern),
              "words in the words list match the above pattern")
    play_hangman_4 = hangman_4(window, WINSIZE, pick_word, valid_pattern,
                               letters_guessed, letters_guessed_incorrect)


def hangman_3(pick_word, letters_guessed, letters_guessed_incorrect):
    """
    This function continues from hangman_2. It prints the dashes with the
    letter revealed in its position of the word if the letter guessed is
    correct. If it is not correct, it reprints the previous print statement,
    adding the incorrect letter to the letters_guessed_incorrect list and
    prints the letters guessed incorrect onto the text window.

    Parameters: pick_word = tbe word from the list that was picked by
                            the function provided in hangman_support.py

                letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the hangman
                                            word
    """
    # this prints the underscores and correct guessed letters
    for j in range(len(pick_word)):
        if j < len(pick_word) - 1:
            print(letters_guessed[j], end='')
        else:
            print(letters_guessed[j])
    print("\n")
    # this prints the incorrectly guessed letters
    for k in range(len(letters_guessed_incorrect)):
        if k < len(letters_guessed_incorrect) - 1:
            print(letters_guessed_incorrect[k], end='')
        else:
            print(letters_guessed_incorrect[k])


def hangman_4(window, WINSIZE, pick_word, valid_pattern, letters_guessed,
              letters_guessed_incorrect):
    """
    This function checks to see if all the letters guessed by the user is the
    hangman word. If it is, the user has won the game, and it asks the
    user to close the graphics window. If the user has guessed the wrong letter
    six times, it then prints that the user has lost the game, revealing what
    the hidden underscored word was, then asking the user to close the graphics
    window. When the window is closed, it will ask the user if they  would like
    to play a game of hangman again.

    Parameters: window = the graphics window with dimensions WINSIZE x WINSIZE
                WINSIZE = the window size from the hangman_support import
                pick_word = tbe word from the list that was picked by
                            the function provided in hangman_support.py
                valid_pattern =  a list of words in the word list that match
                                 the same length as the hangman word and whose
                                 letter match the pattern of the currently
                                 revealed word and the list of incorrect
                                 guesses
                letters_guessed = A list of dashes that change to the
                                  letter guessed if the letter guessed
                                  is in the hangman word
                letters_guessed_incorrect = the list of incorrect user inputed
                                            letters that are not in the hangman
                                            word
    """
    # if the user guesses all the letters correctly, they win and the game ends
    if letters_guessed == pick_word:
        print("\nWinner Winner Chicken Dinner!")
        print("\nClick the graphics window to exit \n")
        Text(Point(WINSIZE * (3/4), WINSIZE * (1/2)),
             'YOU WIN! \n Click the window to exit \n').draw(window)
    elif len(letters_guessed_incorrect) == 6:
    # if the user incorrectly guesses the wrong letter 6 times, they lose and
    # the game ends
        print("\nGame Over, YOU LOSE!\nThe word was", ''.join(pick_word))
        print("\nClick the graphics window to exit \n")
    window.getMouse()
    window.close()


def main():
    file_name = input("Name of input file: ")
    hangmanfile = read_input_file(file_name)
    word_check = valid_word(hangmanfile)  # returns useable words for the game
    if word_check == []:
        print("Error. No valid words")
        exit()
    while True:
        letters_guessed = []  # make list for dashes & letters guessed correct
        letters_guessed_incorrect = []  # set up list for incorrect guesses
        playhangman = input("Would you like to play Hangman? (Type y or n) ")
        if playhangman == "Y" or playhangman == "y":
            play_hangman_1 = hangman_1(word_check,
                                       letters_guessed,
                                       letters_guessed_incorrect)
        elif playhangman == 'N' or playhangman == 'n':
            exit()
main()
