dict = {"apple": 'maçã', 'strawberry': 'morango', 'pineple': 'abacaxi'}
print(dict['strawberry'])
print(dict.values())
print(dict.keys())
print(dict)

print('----dicionário atualizado----')
for key in dict:
    print(f'{key} : {dict[key]}')

dict['banana'] = 'banana'
dict.update({'watermelon':'melância'})

print('----dicionário atualizado----')
for key in dict:
    print(f'{key} : {dict[key]}')

dict.pop('apple')
print('----dicionário atualizado----')
for key in dict:
    print(f'{key} : {dict[key]}')