from math import ceil

class Disciplina:
    def __init__(self, nome, horas, minhas_faltas = None, faltas_max = None):
        self.nome = nome
        self.horas = horas
        self.minhas_faltas = minhas_faltas
        self.faltas_max = faltas_max
        
        
        
    def calcular_faltas(self, horas):
        self.minhas_faltas = 0
        self.faltas_max = horas * 0.25
        self.faltas_max = ceil(self.faltas_max)
        
        return self.faltas_max