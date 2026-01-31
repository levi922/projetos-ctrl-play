class chatBot:
    def __init__(self):
        self.responses = {
            'olá':'Olá! Oque deseja para hoje?',
            'quantos graus internos possui um triangulo?':'um triangulo possui 180°(graus)',
            'em que ano ocorreu a Independência do Brasil?':'a Independência do Brasil foi declarada em 1822',
            'a partir de que idade é permitido se alistar para o exército brasileiro?':'a partir de 18 anos é permitido o alistamento para os cidadões brasileiros',
            'quem é considerado um dos melhores boxeadores da história?':'Muhammad Ali é amplamente considerado por muitos especialistas, fãs e publicações como um dos maiores, senão o maior, boxeador de todos os tempos',
            'qual o maior tornado já registrado no planeta?':'conhecido por ocorrer na cidade de El Reno, Oklahoma, registrou incriveis 4,2 km de extensão sendo avaliado com a classificação de EF3 na escala fujita',
            'qual o jogo mais vendido da história?':'Minecraft, com mais de 300 milhões de cópias vendidas',
            'compositor das soundtracks de call of duty zombies':'seu nome é Kevin Sherwood, sendo responsável por compor musicas desde 2008 até os dias de hoje',
            'resultado de 5x5':'Claro! o resultado desta equação é 25',
            'obrigado pela ajuda':'não foi de nada! estarei aqui caso precise de algo',
            'conte uma piada':'por que os fantasmas são péssimos para contar mentiras? porque são transparentes!',
            'quanto custa um iphone 13?':'os preços variam entre R$3 mil a R$3,5 mil de acordo com os dados mais recentes',
            'qual o god of war mais dificil?':'muitos jogadores confirmam que o primeiro jogo da saga foi o mais difícil de se completar na dificuldade - very hard',
            'melhor mortal kombat para aprender a jogar':'o mortal kombat 9 é reconhecido por sua praticidade para executar combos e sua fluidez para os jogadores',
            'oque o omega representa?':'o Omega, última letra do alfabeto grego, representa fim, conclusão, limite final.'
        }

    def get_response(self,user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, 'desculpe, não entendi, pode repetir a pergunta?')