my_dict = {'Pain' : 1, 'Itachi' : 2, 'Obito' : 3, 'Kisame' : 4, 'Kakuzu' : 5}
print(my_dict)
print(my_dict['Itachi'])
print(my_dict.get('Kakuzu'))
print(my_dict.get('Sasori', 'Такого шиноби нет в списке'))
my_dict.update({'Deydara' : 10, 'Konan' : 11})
s = my_dict.pop('Kisame')
print(s)
print(my_dict)


my_set = {1, 2, 'Itachi', True , False, 5, 5, 2}
print(my_set)
my_set.update(['Sakura', 33])
my_set.discard(2)
print(my_set)