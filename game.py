import display
from globalValues import EXIT

def playGame():
  quit = False
  while not quit: 
    display.clear()
    result = display.playScreen()
    quit = True if result == EXIT else display.endScreen(result)
    display.closeScreen()

