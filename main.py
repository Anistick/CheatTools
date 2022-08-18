import typewrite as type
from apps.ibdw import ibdw_Exec
import time
import os
from colorama import init, Fore as fore

#####################
# CAPYBARA WAS HERE #
# CAPYBARA WAS HERE #
# CAPYBARA WAS HERE #
#####################

type.typewrite(f'{fore.LIGHTYELLOW_EX}Welcome to CheatTools! Please select an option to continue. CheatTools is meant for Windows.', ['.', '!', ','])

def chs():

  options = {'Install Basic DevTools': 1}
  
  os.system('cls')

  for key, value in options.items(): print(f'{fore.GREEN}[{value}] {key}{fore.RESET}')
  
  choice = input('\n> ')
  
  if choice not in str(options.values()):
    print('Invalid choice!')
    time.sleep(1)
    chs()
    
  elif choice == '1':
    ibdw_Exec()
    
chs()