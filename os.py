import os
import time

# in
if 'goo' in 'google.com': 
  print('ok')
else:
  print('fail')
  
os.system("start https://www.google.com")  #! does't work? probably - WSL

time.sleep(5)

address = input('File: ')  
os.startfile('./types.py')
os.startfile(address)