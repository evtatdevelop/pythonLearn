result = ''
string = input('String: ')
for i in string:
  if i == ' ':
    continue
  elif i == '.' or i == ',' or i == '-':
    i = '_'
  else:
    result += i
else:
  print('DONE!')
print('RESULT: ' + result + ' (' + str(len(result)) + ').')
