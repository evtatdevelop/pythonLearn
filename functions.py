import os
import time

def checkAge(age=''):
  if age == '':
    return 9999999999999
  return int(float(age) * 24*60*60)

def dataSet():
  return input('Search: '), checkAge(input('Age(dd): '))

def search(data=['', 9999]):
  result = []
  for addr, dirs, files in os.walk('/home'):
    for file in files:
      fullPath = os.path.join(addr, file)
      if data[0] in fullPath and time.time() - os.path.getctime(fullPath) < data[1]:
        result.append(fullPath)
  return result

def getLine(pathFile=''):
  return('\n' + pathFile)

def showResults(list=['no data']):
  for item in list:
    print(getLine(item))

showResults(search(dataSet()))
