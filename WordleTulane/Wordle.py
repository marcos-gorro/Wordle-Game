#Tulane University, CMPS 1500, Fall 2023
#
#STUDENTS MUST FILL IN BELOW
#
#Student name:
#Student email address:
#
#Collaborators:

# NOTE: you must write your own code. You may discuss the assignment with 
#       professors, TAs, other students, or family members. But you MUST
#       list anyone you collaborated with in the space above.

# ALSO: You must add comments below which explain how your solution works.
#       If you do not do this, your solution will not receive credit.
import random

from WordleWordlist import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def enter_action(guessedword):
    """ This function is called any time the enter button 
    is clicked/typed in the game. guessedword is the player's most 
    recent guess which needs to be checked. 
    """

    # Milestone 0.5: put test code here to display
    #                the solution on game board using:
    #gw.set_square_letter(row, col, letter)

    # also show a message on the gameboard indicating that this is for milestone 1
    gw.show_message("milestone 1") # replace this
    # end milestone 0

    # Milestones 1+: put code below here (make sure it is indented)
    #Milestone 1-4 complete
    guessedword = guessedword.lower()

    row = gw.get_current_row()
    if guessedword in FIVE_LETTER_WORDS:
        letterused = [False]*len(guessedword) #list to determine whether the letters are used
        guesslist=list(guessedword) #list of each list in guess
        solutionlist=list(solution) #list of each letter in solution4
        #First sets all letters in guess to grey
        for column in range(N_COLS):
                gw.set_square_color(row, column, MISSING_COLOR)
                gw.set_key_color(gw.get_square_letter(row, column), MISSING_COLOR)
        #then sets all letters in guess that are in the right position to green
        for column in range(N_COLS):
            if guesslist[column] == solutionlist[column]:
                gw.set_square_color(row, column, CORRECT_COLOR)
                gw.set_key_color(gw.get_square_letter(row, column), CORRECT_COLOR)
                letterused[column]= True #to show a letter has been used up
                guesslist[column]= None #gets rid of letter that is in correct position
                solutionlist[column]= None #gets rid of the letter guessed correctly
        #finally sets letters that are in the word but not the right position to yellow
        for column in range(N_COLS):
            if guesslist[column] is not None:
                if guesslist[column] in solutionlist:
                    for j in range(len(guessedword)):
                        if solutionlist[j]==guesslist[column] and not letterused[j]:
                            gw.set_square_color(row, column, PRESENT_COLOR)
                            letterused[j]= True # to show the letter in position j of guessed word has been used
                            solutionlist[j]= None #show that the letter has been used up in the solution
                            guesslist[column] = None # show that the letter has been used up in the guess
                            if gw.get_key_color(gw.get_square_letter(row, column))!= CORRECT_COLOR:
                                gw.set_key_color(gw.get_square_letter(row, column), PRESENT_COLOR)
                            break

         #makes a list of possible words and removes words based on the guess
        letterused = [False] * len(guessedword)
        guesslist = list(guessedword)
        for col in range(len(guessedword)):
            if gw.get_key_color(gw.get_square_letter(row ,col))== MISSING_COLOR:
                for possible_word in possible_words.copy():
                    if gw.get_square_letter(row , col).lower() in possible_word:
                        possible_words.remove(possible_word)
            if gw.get_key_color(gw.get_square_letter(row ,col))== PRESENT_COLOR and gw.get_square_color(row ,col)== MISSING_COLOR:
                for possible_word in possible_words.copy():
                    if gw.get_square_letter(row , col).lower() not in possible_word or gw.get_square_letter(row,col).lower() == possible_word[col]:
                        possible_words.remove(possible_word)
            if gw.get_square_color(row ,col)== CORRECT_COLOR:
                for possible_word in possible_words.copy():
                    if gw.get_square_letter(row , col).lower() != possible_word[col]:
                        possible_words.remove(possible_word)
            if gw.get_square_color(row, col) == PRESENT_COLOR:
                for possible_word in possible_words.copy():
                    if gw.get_square_letter(row , col).lower() not in possible_word or gw.get_square_letter(row , col).lower()==possible_word[col]:
                        possible_words.remove(possible_word)
        print(f'There are {len(possible_words)} words left: {possible_words}')
        if guessedword == solution:
            gw.show_message("Congratulations!!")
            solved=True
        else:
            gw.show_message("Keep Trying!!")
            row+=1
            gw.set_current_row(row)
            solved=False
    else:
        gw.show_message("Not in word list")

# Milestone 0: chose a random word from the wordlist here
solution=random.choice(FIVE_LETTER_WORDS)
possible_words = FIVE_LETTER_WORDS.copy()
#print(solution)


# Students: do not change anything below here
gw = WordleGWindow()
gw.add_enter_listener(enter_action)