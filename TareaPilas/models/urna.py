# Models/urna.py

class UrnaDigital:
    def __init__(self):
        self.votos = []

    def registrar_voto(self, voto):
        self.votos.append(voto)

    def eliminar_ultimo_voto(self):
        if self.votos:
            return self.votos.pop()
        return None

    def ultimo_voto(self):
        if self.votos:
            return self.votos[-1]
        return None

    def mostrar_todos_votos(self):
        return self.votos
