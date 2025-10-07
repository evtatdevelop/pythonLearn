v = None
print(v, type(v) )
v = 1
print( type(v) )
v = 1.0
print(v, type(v) )
v = 1 + 1j
print(v, type(v) )
v = '1'
print(v, type(v) )
v = [1, 2, 'three']
print(v, type(v) )
v = (1, 2, 'three')
print(v, type(v) )
v = {1, 2, 'three'}
print(v, type(v) )
v = {'one': 1, 'two': 2}
print(v, type(v) )
v = True
print(v, type(v) )

# examples

x = float(input('First num: ') )
y = float(input('Second num: ') )

if int(x) == x and int(y) == y: 
  result = int(x + y)
else: 
  result = x + y

print('Result: ' + str(result))
