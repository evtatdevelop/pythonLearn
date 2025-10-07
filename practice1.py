import os
import time

serach = input('Search: ')
fileAge = float(input('Age(dd): '))

pathList = []
for addr, dirs, files,  in os.walk('..'):
  for file in files:
    fullPath = os.path.join(addr, file)

    if serach in fullPath and time.time() - os.path.getctime(fullPath) < int(fileAge * 24 * 60 * 60):
      pathList.append( fullPath )


for pathFile in pathList:
  print('\n' + pathFile)
  