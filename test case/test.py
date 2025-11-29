import unittest
from operacao import Operacao
# operacao(com letra minuscula) é do arquivo; Operacao(com letra maiuscula)
#é a classe dentro do arquivo
class TestOperacao(unittest.TestCase):
    def test_somasuc(self):
        res = Operacao.somasuc(4,5)
        self.assertEqual(res, 9)

    def test_somafalsa(self):
        res = Operacao.somafalsa(4,5)
        self.assertEqual(res, 9)

unittest.main(argv=[''],exit=False)