from os import system, name 
import words
from globalValues import VALID_GUESS, EXIT, WON, LOST
from helper import validateGuess, confirmWordCorrect

HANGMANPICS = [[
'                 +---+  ',
'                 |   |  ',
'                     |  ', 
'                     |  ', 
'                     |  ', 
'                     |  ',
'               ========='],[
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                     |  ', 
'                     |  ', 
'                     |  ',
'               ========='], [
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                 |   |  ', 
'                     |  ', 
'                     |  ',
'               ========='], [
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                /|   |  ', 
'                     |  ', 
'                     |  ',
'               ========='], [
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                /|\  |  ', 
'                     |  ', 
'                     |  ',
'               ========='],[
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                /|\  |  ', 
'                /    |  ', 
'                     |  ',
'               ========='], [
'                 +---+  ',
'                 |   |  ',
'                 O   |  ', 
'                /|\  |  ', 
'                / \  |  ', 
'                     |  ',
'               =========']]

#playscreen segments
def gallows (pic):
  for section in range(0, len(HANGMANPICS[pic])):
    print (HANGMANPICS[pic][section])

def clear():
    # for windows 
  msg = 'cls' if name == 'nt' else 'clear'
  _ = system(msg) 

def AlreadyGuessed(already_guessed_letter, guess = ''):
  display = 'Already Guessed \n        Guess: '+ str(guess)+'\n        +-------------------+\n'
  for index, letter in enumerate(already_guessed_letter, start=1):
    if index == 1:
      display += '        |'
    if index%9 == 0:
      display += " " + letter + ' |\n'         
      if index != len(already_guessed_letter):
       display += "        |"
    else:
      display += " " + letter 
      if index == len(already_guessed_letter):
        for spacer in range (0, 19-(2*(index % 9))):
          display += ' '
        display += '|\n'
  display += "        +-------------------+\n"    
  print (display)  

def chooseLetter (message):
  print("\n"+ message + "\nChoose A letter: (type exit to quit)")
  guessed_letter = input().lower()
  return guessed_letter

def WordCompletion (chosen_word, already_guessed_letter):
  display = '\n          '
  for letter in chosen_word:
    if letter in already_guessed_letter:
      display += letter + ' '
    else:
      display += '_ '  
  print (display)

#various screens
def closeScreen():
  clear()
  print ("Thank you for playing come back soon")

def endScreen (won):
  print ('You Won') if won == WON else print('You Lost')  
  again_input = ''
  while not (again_input == 'y' or again_input == 'yes' or again_input == 'ye' or   again_input == 'ys' or again_input == 'n' or again_input == 'no' ):
    again_input = input("play again y/n? ").lower()
  if again_input == 'n' or again_input == 'no':
    return True
  return False  

def playScreen():
  chosen_word = words.chooseAWord()
  guessed_letter = ''
  already_guessed_letter = []
  failed_guess = 0
  
  guess_result = ''
  while True: 
    AlreadyGuessed(already_guessed_letter, guessed_letter)
    gallows(failed_guess)
    WordCompletion(chosen_word, already_guessed_letter)

    guessed_letter = chooseLetter(guess_result)
    
    guess_result = validateGuess(guessed_letter, already_guessed_letter)
    
    if (guess_result == EXIT):
      return EXIT
    if (guess_result == VALID_GUESS):
      if not guessed_letter in already_guessed_letter:
        already_guessed_letter.append(guessed_letter)  
      if not guessed_letter in chosen_word:
        failed_guess +=1
        if failed_guess > 6: 
          return LOST
      else:
        if confirmWordCorrect(chosen_word, already_guessed_letter):
          return WON           
    clear()