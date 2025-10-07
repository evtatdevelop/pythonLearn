var = 45
array = [1, 'one', var, [var, 'first'], ]

array[0], array[2], array[3] = array[3], array[2], array[0]
print(array) 

array[0], array[2], array[3] = array[0], array[0], array[0]
print(array) 

array += array
print(array) 

array *= 2
print(array) 

array = list('A mother washed a window')
print(array) 

array = list(range(1, 36, 7))
print(array) 

odd = []
even = []
for i in array:
  if i % 2 == 0:
    # odd += [i]
    odd.append(i)
  else:
    # even += [i]
    even.append(i)
print(odd) 
print(even) 


clone_array_1 = array.copy()
print('clone_array_1: ', clone_array_1)

clone_array_2 = array[::]
print('clone_array_2: ', clone_array_2)

clone_array_part = array[1:4:]
print('clone_array_part: ', clone_array_part)

even_2 = array[::2]
print('even_2: ', even_2)

odd_2 = array[1::2]
print('odd_2: ', odd_2)

clone_array_ = array[3:]
print('clone_array_: ', clone_array_)
