print('Hi there!')

var_1, var_2 = 'test', 17
print(var_1, var_2)

var_1, var_2 = var_2, var_1
print(var_1, var_2)

var_1 += 21
print(var_1)

array = ['one', 'two', 3, var_1, [1,2,3], ]
print(array)

one, two, three, var, subArr = array
print(one)
print(two)
print(three)
print(subArr)

*strings, number, array = array
print(strings)
print(number)
print(array)
