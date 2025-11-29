#projeto original aluno.py
class Aluno:
    def __init__(self, nome, RA, nota1, nota2, média):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2
        self.média = (nota1+nota2)/2
    
    def ficha_aluno(self):
        self.valores()
        self.calculo_média()

    def valores(self):
        print(f'---- ficha de identificação ----')
        print(f'nome:{self.nome}')
        print(f'Registro de aluno:{self.RA}')

    def calculo_média(self):
        print(f'primeira nota:{self.nota1}')
        print(f'segunda nota:{self.nota2}')
        print(f'média:{self.média}')

        
    pass

FI = Aluno(nome= input('nome:'), RA= input('RA:'), nota1= int(input('sua nota 1:')), nota2= int(input('sua nota2:')), média= '')

FI.ficha_aluno()
