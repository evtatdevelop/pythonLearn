my_tuple = (9, 7, 5, ) #? unchangeble (safe data)
print(my_tuple)

a,b,c = my_tuple
print(a,b,c)

tupToList = list(my_tuple)
print(tupToList)

for i in range(len(tupToList)):
  tupToList[i] *= -1

new_tuple = tuple(tupToList)
print(new_tuple)

my_tuple_duble = my_tuple
my_tuple += (999, 'newNum')
print(my_tuple)
print(my_tuple_duble)