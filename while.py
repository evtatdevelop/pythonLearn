result = ''
while True:
  string = input('Input: ')
  if string == 'exit' or string == 'stop':
    break
  result += string

print('Done: ' + result + ', length: ' + str(len(result)))  
