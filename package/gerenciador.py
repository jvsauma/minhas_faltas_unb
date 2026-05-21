from package.disciplina import Disciplina
from package.limpeza import Limpeza

class Gerenciador:
    def __init__(self):
        
        self.disciplinas = []
        self.limpeza = Limpeza()
        
        
    def criar_lista_ordenada(self):
        
        lista_materias = []
        
        #criando uma lista em ordem alfabética das disciplinas
        for materia in self.disciplinas:
            
            lista_materias.append(materia)
            
            
            lista_materias.sort(key = lambda dicionario : dicionario["nome"])
    
        #lista de dicionários
        return lista_materias
    
        
    def lembrete(self):
        
        return print("\nLEMBRANDO: Escreva o nome da matéria exatamente como ela está registrada.")
    
    
    
    def adicionar_disciplina(self):
        nome = input("\nDigite o nome da disciplina: ").strip()
        
        for dicionar in self.disciplinas:
            if dicionar["nome"] == nome:
                print("\nDisciplina já existente.")
                return
        
        horas = input("\nDigite as horas da disciplina (somente números): ").strip()
        
        try:
            horas = int(horas)
        except:
            print("\nSó é permitido números.")
            return
        
        #verificação de existencia em lista de disciplinas
        
        materia = Disciplina(nome, horas)
        materia.calcular_faltas(horas)
        dict_materia = materia.__dict__
        self.disciplinas.append(dict_materia)
        
        self.limpeza.limpar_terminal()
        print("\nSua disciplina foi adicionada!")

        
    
    
    def remover_disciplina(self):

        #lista de dicionários
        lista_materias = self.criar_lista_ordenada()

        if not lista_materias:
            print("\nNão existe disciplina para retirar.")
            return
        
        
        print("\nIndex - Disciplina")
        
        for dicionar in lista_materias:
            print(f"\n[{lista_materias.index(dicionar)}] - {dicionar["nome"]}")


        disciplina_remove_disciplina = input("\nQual disciplina você deseja remover? (Digite o número referente): ").strip()
        
        
        try:
            disciplina_remove_disciplina = int(disciplina_remove_disciplina)
        except:
            print("Digite somente números")
            return
        
        
        #verificação de existencia em lista de disciplinas
        for dicionar in lista_materias:
            if disciplina_remove_disciplina == lista_materias.index(dicionar) and dicionar["nome"] == lista_materias[disciplina_remove_disciplina]["nome"]:
                
                
                self.disciplinas.remove(dicionar)
                
                
                self.limpeza.limpar_terminal()
                print("\nDisciplina removida")
                return
        
        self.limpeza.limpar_terminal()
        print("\nDisciplina não encontrada")
        
    
    
    def adicionar_faltas(self):
        
        #lista dicionários
        lista_materias = self.criar_lista_ordenada()
        
        print("\nIndex - Disciplina / Faltas / Faltas Max")
        
        for dicionar in lista_materias:
            print(f"\n[{lista_materias.index(dicionar)}] - {dicionar["nome"]} / {dicionar["minhas_faltas"]} / {dicionar["faltas_max"]}")


        disciplina_add_falta = input("\nQual disciplina deseja adicionar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            disciplina_add_falta = int(disciplina_add_falta)
            
        except:
            print("Digite apenas o número referente à disciplina.")
            return
        
        
        
        for dicionar in lista_materias:
        
            if disciplina_add_falta == lista_materias.index(dicionar):
                
                print(f"\nDisciplina selecionada: {dicionar["nome"]}")
                
                qtd_faltas = input("\nQuantas faltas deseja adicionar? (somente números): ")
                
                try:
                    qtd_faltas = int(qtd_faltas)
                    
                except:
                    print("\nSelecione apenas números")
                    return
                
                dicionar["minhas_faltas"] += qtd_faltas
                self.limpeza.limpar_terminal()
                print("\nFaltas adicionadas com sucesso!")
                return
            
        self.limpeza.limpar_terminal()
        print("\nMatéria não encontrada.")
        return
        

    
    def retirar_faltas(self):

        lista_materias = self.criar_lista_ordenada()

        print("\nIndex - Disciplina / Faltas / Faltas Max")
        
        
         #arrumar isso para lógica de retirar matéria
        for dicionar in lista_materias:
            print(f"\n[{lista_materias.index(dicionar)}] - {dicionar["nome"]} / {dicionar["minhas_faltas"]} / {dicionar["faltas_max"]}")


        disciplina_remove_falta = input("\nQual disciplina deseja retirar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            disciplina_remove_falta = int(disciplina_remove_falta)
            
        except:
            print("Digite apenas o número referente à disciplina.")
            return
        
        
        
        for dicionar in lista_materias:
        
            if disciplina_remove_falta == lista_materias.index(dicionar):
                
                print(f"\nDisciplina selecionada: {dicionar["nome"]}")
                
                qtd_faltas = input("\nQuantas faltas deseja retirar? (somente números): ")
                
                try:
                    qtd_faltas = int(qtd_faltas)
                    
                except:
                    print("\nSelecione apenas números")
                    return
                
                
                #arrumar isso e arrumar matérias com mesmo nome
                dicionar["minhas_faltas"] -= qtd_faltas
                self.limpeza.limpar_terminal()
                print("\nFaltas retiradas com sucesso!")
                
            else:
                self.limpeza.limpar_terminal()
                print("\nMatéria não encontrada.")
                return

            
        