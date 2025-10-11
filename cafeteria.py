print('menu da cafeteria')
dict = {'expresso': '7.00', 'Pingado': '9.00', 'Pão na chapa': '11.00', 'Achocolatado': '13.00', 'Misto quente': '15.00'}
print(dict.values())
print(dict.keys())
while True:
    for key in dict:
        input(key).lower
        int(input('Quantidade:'))
        