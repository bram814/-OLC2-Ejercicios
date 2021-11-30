
class Entorno():
    def __init__(self, ant):
        self.ant = ant
        self.tabla = {}

    def add(self, simbolo):
        sim = self.get(simbolo.id)
        if sim == None:
            self.tabla[simbolo.id] = simbolo
        else:
            print("Error: variable ", sim.id, " ya definida")

    def get(self, id):
        ent = self
        while ent != None:
            if id in ent.tabla:
                return self.tabla[id]
            ent = ent.ant
        print("Error: variable ", id, " no definida")
        return None
