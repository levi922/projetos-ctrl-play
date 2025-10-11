import turtle
import time
continuar = True
def init_screen():
    turtle.Screen().setup(1.0, 1.0)
def selecao(opcao):
    if(opcao == 4):
        global continuar
        continuar = False
        print('voce saiu')
    elif ( opcao == 1):
        desenha_quad(int(input('entre com tamanho:')))
    elif ( opcao == 2):
        desenha_circ(int(input('entre com o raio:')))
    elif ( opcao == 3):
        desenha_triangle(int(input('entre com o tamanho:')))

def desenha_triangle(tamanho):
    time.sleep(2)
    for _ in range(3):
        turtle.forward(tamanho)
        turtle.left(120)
    time.sleep(3)
    turtle.clear()

def desenha_circ(raio):
    turtle.circle(raio)
    time.sleep(3)
    turtle.clear()

def desenha_quad(tamanho):
    time.sleep(2)
    for _ in range(4):
        turtle.forward(tamanho)
        turtle.right(90)
    time.sleep(3)
    turtle.clear()
while continuar:
    init_screen()
    print('---- desenhar forma ----')
    print('1 - quadrado')
    print('2 - circulo')
    print('3 - triangulo')
    print('4 - sair')
    opcao = int(input('entre com o numero da opcao: '))
    selecao(opcao)
