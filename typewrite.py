import sys
import time

def typewrite(text, delaychars):
  
  for char in text:

    if char in delaychars:
      print(char, end = '')
      time.sleep(0.5)
      
    else:
      print(char, end = '')
      time.sleep(0.05)
      
    sys.stdout.flush()
    
typewrite('', [''])