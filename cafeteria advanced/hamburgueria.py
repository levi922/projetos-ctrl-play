hamburgueria = {
    'xburguer': 14.00,
    'xbacon': 18.00,
    'xtudo': 29.00,
    'milkshake':12.00,
    'refrigerante':10.00
}

def menu():
    print('\n🍔 menu')
    for item, preco in hamburgueria.items():
        print(f'- {item}: R$ {preco:.2f}')

def pedir_quantidade():
    while True:
        try:
            quantidade = int(input('quantidade:'))
            if quantidade > 0:
                return quantidade
            else:
                print('digite um número maior que zero')
        except:
            print('digite apenas números inteiros')
            
def hamburgueria_programa():
    total = 0

    print('bem-vindo a hamburgueria')

    menu()
    while True:
        pedido = input("\n digite o item que deseja(ou 'sair'):").lower()

        if pedido == 'sair':
           break

        if pedido in hamburgueria:
            quantidade = pedir_quantidade()
            i= input('\n deseja adicionar o cupom de 10% à compra?')

            subtotal = hamburgueria[pedido]* quantidade

            if(i == 'sim'):
                subtotal *= 0.90
                print('cupom de 10% adicionado a compra')
            else:
                print('compra finalizada')
            total += subtotal

            print(f'{quantidade}x {pedido}= R$ {subtotal:.2f}')
            T= print(f'Total parcial: R$ {total:.2f}')

        else:
            print('item não encontrado no cardapio.')
    print(f'\n 💰Total da compra: R$ {total:.2f}')
    print('obrigado pela preferência!')

hamburgueria_programa()