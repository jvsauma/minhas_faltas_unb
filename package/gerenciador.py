from package.disciplina import Disciplina

class Gerenciador:
    def __init__(self):
        
        self.disciplinas = []
        
    def lembrete(self):
        
        return print("\nLEMBRANDO: Escreva o nome da matéria exatamente como ela está registrada.")
    
    
    
    def adicionar_disciplina(self):
        nome = input("\nDigite o nome da disciplina: ")
        horas = input("\nDigite as horas da disciplina (somente números): ")
        
        try:
            horas = int(horas)
        except:
            return print("\nSó é permitido números.")
        
        #verificação de existencia em lista de disciplinas
        for d in self.disciplinas:
            if d.nome == nome:
                print("\nDisciplina já existente.")
                return
        
        materia = Disciplina(nome, horas)
        materia.calcular_faltas(horas)
        self.disciplinas.append(materia)
        
        return print("\nSua disciplina foi adicionada!")

        
    
    
    def remover_materia(self):

        if not self.disciplinas:
            return print("\nNão existe disciplina para retirar")
        
        nome = input("\nDigite o nome exato da disciplina que deseja remover: ")
        
        #verificação de existencia em lista de disciplinas
        for d in self.disciplinas:
            if nome == d.nome:
                self.disciplinas.remove(d)
                
                return print("\nDisciplina removida")
        
        print("\nDisciplina não encontrada")
        
    
    
    def adicionar_faltas(self):

        disciplina_add_falta = input("\nQual disciplina deseja adicionar a(s) falta(s)? ")
        
        for materia in self.disciplinas:
            
            if materia.nome == disciplina_add_falta:
                print(f"\nDisciplina selecionada: {disciplina_add_falta}")
                qtd_faltas = int(input("\nQuantas faltas deseja adicionar? (somente números): "))
                materia.minhas_faltas += qtd_faltas
                print("\nFaltas adicionadas com sucesso!")
                
            else:
                print("\nMatéria não encontrada.")
        
        
        
        
        
        pass
    
    def retirar_faltas(self):

        disciplina_remove_falta = input("\nQual disciplina deseja retirar as faltas?")
        
        for materia in self.disciplinas:
            
            if materia.nome == disciplina_remove_falta:
                print(f"\nDisciplina selecionada: {disciplina_remove_falta}")
                qtd_faltas = int(input("\nQuantas faltas deseja retirar? (somente números) "))
                materia.minhas_faltas -= qtd_faltas
                print("\nFaltas retiradas com sucesso")

            
        pass