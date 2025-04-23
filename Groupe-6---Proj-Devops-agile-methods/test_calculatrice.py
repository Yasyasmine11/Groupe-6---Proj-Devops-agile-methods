import unittest
import tkinter as tk
from main import Calculatrice

class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # cache la fenêtre pendant les tests
        self.calc = Calculatrice(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        self.calc.clear()
        self.calc.ajouter('2')
        self.calc.ajouter('+')
        self.calc.ajouter('3')
        self.calc.evaluer()
        self.assertEqual(self.calc.entry.get(), '5')

    def test_multiplication(self):
        self.calc.clear()
        self.calc.ajouter('4')
        self.calc.ajouter('*')
        self.calc.ajouter('6')
        self.calc.evaluer()
        self.assertEqual(self.calc.entry.get(), '24')

    def test_division_par_zero(self):
        self.calc.clear()
        self.calc.ajouter('10')
        self.calc.ajouter('/')
        self.calc.ajouter('0')
        self.calc.evaluer()
        self.assertEqual(self.calc.entry.get(), 'Erreur')

    def test_parentheses(self):
        self.calc.clear()
        for char in "(2+3)*4":
            self.calc.ajouter(char)
        self.calc.evaluer()
        self.assertEqual(self.calc.entry.get(), '20')

    def test_clear(self):
        self.calc.ajouter('123')
        self.calc.clear()
        self.assertEqual(self.calc.entry.get(), '')

if __name__ == '__main__':
    unittest.main()

# python -m unittest test_calculatrice.py