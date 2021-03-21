import re

from globalValues import EXIT, INVALID_GUESS, ALREADY_GUESS, VALID_GUESS

def validateGuess (guess, already_guessed):
  if (guess.lower() == EXIT.lower()):
    return EXIT
  if (re.search("[^a-z]", guess)) or len(guess) != 1 :
      return INVALID_GUESS
  if guess in already_guessed:
    return ALREADY_GUESS   
  return VALID_GUESS

def confirmWordCorrect (chosen_word, already_guessed_letter):
  won_word = []
  for letter in chosen_word:
    if letter in already_guessed_letter:
      won_word.append(letter)
  if len(won_word) ==  len(chosen_word):
    return True
  return False