print('operações disponiveis: 1= +, 2= -, 3= x, 4= /')
def opcao(selec):
    if (selec == 1):
        res = soma(int(input('valor da soma:')), int(input('segundo valor:')))
        print(res)
    elif (selec == 2):
       res = subtracao(int(input('valor da subtração:')), int(input('segundo valor:')))
       print(res)
    elif (selec == 3):
       res = multiplicacao(int(input('valor da multiplicação:')), int(input('segundo valor:')))
       print(res)
    elif (selec == 4):
        res = divisao(int(input('valor da divisão:')), int(input('segundo valor:')))
        print(res)

def soma(a, b):
    return(a+b)

def subtracao(a, b):
    return(a-b)

def multiplicacao(a, b):
    return(a*b)

def divisao(a, b):
    return(a/b)

selec = int(input("entre com a opção: "))
opcao(selec)
