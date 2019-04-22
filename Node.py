class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.generador = {}
        self.evaluado = False
        self.terminal = False
        self.isInicial = False
    
    def getGenerador(self):
        return self.generador
    
    def getNombre(self):
        return self.nombre
    
    def setGenerador(self,generador):
        self.generador = generador
    
    def setEvaluado(self):
        self.evaluado = True
    
    def getEvaluado(self):
        return self.evaluado
    
    def setIsTerminal(self):
        self.terminal = True
    
    def setIsIinicial(self):
        self.isInicial = True
    
    def isTerminal(self):
        return self.terminal
    
    def getIsIinicial(self):
        return self.isInicial

        


   