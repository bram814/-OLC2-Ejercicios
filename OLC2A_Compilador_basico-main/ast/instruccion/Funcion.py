from entorno.simbolo import Simbolo

class Funcion():
    def __init__(self, id, Lsent, tipo, linea):
        self.id = id
        self.Lsent = Lsent
        self.tipo = tipo
        self.linea = linea

    def reconcerFunciones(self, ent):
        simbolo = ent.get(self.id)
        if simbolo == None:
            nsimbolo = Simbolo(self.id, self.tipo, self)
            ent.add(self.id, nsimbolo)

    def ejecutar(self, ent):
        simbolo = ent.get(self.id)
        if simbolo == None:
            print("la funcion no se encontro")
        else:
            self.Lsent.ejecutar(ent)