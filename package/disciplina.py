from math import ceil

class Disciplina:
    def __init__(self, nome, horas, minhas_faltas = 0, faltas_max = 0, id = None):
        self.id = id
        self.nome = nome
        self.horas = horas
        self.minhas_faltas = minhas_faltas
        self.faltas_max = faltas_max
        
        
        
    def calcular_faltas(self, horas):
        self.minhas_faltas = 0
        self.faltas_max = ceil(horas * 0.25)
        
        return self.faltas_max