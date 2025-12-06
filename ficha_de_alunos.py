m = print('---- opções para ficha dos alunos ----','aperte 1 para terminar o cadastro','caso queira continuar, continue','colocando as informações')
print(m)
class LA: #Lista de Alunos
    def __init__(self, nome, RA, nota1, nota2):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2

    def aluno(self):
         print(f'---- ficha do aluno ----')
         print(f'nome:{self.nome}')
         print(f'Registro de aluno:{self.RA}')
         print(f'primeira nota:{self.nota1}')
         print(f'segunda nota:{self.nota2}')
         print(f'média:{(self.nota1+self.nota2)/2}')

listaAlunos = []

while True:
    FI = LA(nome= input('nome:'), RA= input('RA:'), nota1= int(input('sua nota 1:')), nota2= int(input('sua nota2:')))
    FI.aluno()
    if(FI == '1'):
        print('lista de alunos:'(listaAlunos))
        print(m)
        break
    else:
        continue
