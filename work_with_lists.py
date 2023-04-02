my_list = ['audi', 'bmw', 'toyota']
my_list2 = ['aston martin', 'porsche']
number_list = [12, 3, 7, 7, 64, 17, 28, 4, 28]
print(my_list)

my_list.append('lada')
print(my_list)

my_list.insert(1, 'mercedes')
print(my_list)

my_list.remove('lada')
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(my_list.count('bmw'))

my_list.extend(my_list2)
print(my_list)

new_list = my_list.copy()
print(new_list)

print(my_list.pop(0))
print(my_list.pop())
print(my_list)

my_list.clear()
print(my_list)

number_list = list(set(number_list))
print(number_list)

numbers = [1, 2, 2, 3, 4, 4, 1]
result = []
for i in numbers:
    if i not in result:
        result.append(i)

print(result)
