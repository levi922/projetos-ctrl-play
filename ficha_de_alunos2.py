print('---- opções para ficha dos alunos ----')
print('Aperte 1 para terminar o cadastro')
print('Caso queira continuar, continue colocando as informações')
print('---------------------------------------')

class LA:  # Lista de Alunos
    def __init__(self, nome, RA, nota1, nota2):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2

    def aluno(self):
        print('---- ficha do aluno ----')
        print(f'Nome: {self.nome}')
        print(f'Registro de aluno: {self.RA}')
        print(f'Primeira nota: {self.nota1}')
        print(f'Segunda nota: {self.nota2}')
        print(f'Média: {(self.nota1 + self.nota2) / 2}')


listaAlunos = []

while True:
    print("\nDigite os dados do aluno:")
    nome = input("Nome: ")

    # Verifica se quer parar
    if nome == "1":
        break

    RA = input("RA: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))

    FI = LA(nome, RA, nota1, nota2)
    FI.aluno()

    listaAlunos.append(FI)  # adiciona o aluno na lista

print("\n---- LISTA DE ALUNOS CADASTRADOS ----")
for aluno in listaAlunos:
    aluno.aluno()