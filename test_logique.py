import unittest
from logique import CalculatriceLogique

class TestCalculatriceLogique(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatriceLogique()

    def test_addition(self):
        self.calc.ajouter('2')
        self.calc.ajouter('+')
        self.calc.ajouter('3')
        self.assertEqual(self.calc.evaluer(), '5')

    def test_multiplication(self):
        self.calc.ajouter('4')
        self.calc.ajouter('*')
        self.calc.ajouter('5')
        self.assertEqual(self.calc.evaluer(), '20')

    def test_division_par_zero(self):
        self.calc.ajouter('10')
        self.calc.ajouter('/')
        self.calc.ajouter('0')
        self.assertEqual(self.calc.evaluer(), 'Erreur')

    def test_parentheses(self):
        for char in "(2+3)*4":
            self.calc.ajouter(char)
        self.assertEqual(self.calc.evaluer(), '20')

    def test_clear(self):
        self.calc.ajouter('123')
        self.calc.clear()
        self.assertEqual(self.calc.equation, '')

if __name__ == '__main__':
    unittest.main()
