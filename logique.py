class CalculatriceLogique:
    def __init__(self):
        self.equation = ""

    def ajouter(self, char):
        self.equation += str(char)

    def evaluer(self):
        try:
            return str(eval(self.equation))
        except:
            return "Erreur"

    def clear(self):
        self.equation = ""
