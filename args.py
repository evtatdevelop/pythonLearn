###
def func(*args):
  print(args)

func('first', 134, [1,2,3])

###
def func1(param, *args):
  print(param)
  print(args)

func1('first', 134, [1,2,3])

###
def func2(param, param1=7, *args, key):
  print(param, param1)
  print(args)
  print(key)

func2('first', 134, 17, 'test', [1,2,3], key=True)

#example
def getSet(*args, sort=False):
  result = []
  for arg in args:
    for item in arg:
      if item not in result:
        result.append(item)
  if sort == "up" or sort == "Up" or sort == "down" or sort == "Down":
    result.sort()
  if sort == "down" or sort == "Down":
    result.reverse()
  return result
  
print('\nExample')
a = [3,5,6,8,2,4,7]
b = [0,6,3,7,1,]
c = [4,7,9,3,9]
print( getSet(a, b, c) )
print( getSet(a, b, c, sort='Up') )
print( getSet(a, b, c, sort ='Down') )