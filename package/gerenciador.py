from package.disciplina import Disciplina
from package.limpeza import Limpeza
from package.banco_de_dados import BancoDeDados

class Gerenciador:
    def __init__(self):
        
        self.limpeza = Limpeza()
        self.banco = BancoDeDados()
    
        
    def lembrete(self):
        
        return print("\nLEMBRANDO: Escreva o nome da matéria exatamente como ela está registrada.")
    
    
    
    def adicionar_disciplina(self):
        nome = input("\nDigite o nome da disciplina: ").strip()
        
        if self.banco.verificar_nome(nome):
            print("\nDisciplina já existente.")
            return
        
        horas = input("\nDigite as horas da disciplina (somente números): ").strip()
        
        try:
            horas = int(horas)
        except:
            print("\nSó é permitido números.")
            return
        
        
        materia = Disciplina(nome, horas)
        max_faltas = materia.calcular_faltas(horas)
        self.banco.salvar_disciplina(nome, horas, 0, max_faltas)
        
        self.limpeza.limpar_terminal()
        print("\nSua disciplina foi adicionada!")

    
    
    def remover_disciplina(self):

        if not self.banco.verificar_tabela():
            print("\nNão existe disciplina para retirar.")
            return
        
        
        print("\nId - Disciplina")

        self.banco.listar_disciplinas("id")

        disciplina_remove_disciplina = input("\nQual disciplina você deseja remover? (Digite o id referente): ").strip()
        
        
        try:
            disciplina_remove_disciplina = int(disciplina_remove_disciplina)
        except:
            print("Digite somente números")
            return
        
        if self.banco.verificar_id(disciplina_remove_disciplina):
            self.banco.remover_disciplina(disciplina_remove_disciplina)
            
            self.limpeza.limpar_terminal()
            print("\nDisciplina removida")
            return
        
        self.limpeza.limpar_terminal()
        print("\nDisciplina não encontrada")
        
    
    
    def adicionar_faltas(self):
        
        print("\nIndex - Disciplina / Horas / Faltas / Faltas Max")
        
        self.banco.listar_disciplinas("sem_id")

        disciplina_add_falta = input("\nQual disciplina deseja adicionar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            disciplina_add_falta = int(disciplina_add_falta)
            
        except:
            print("Digite apenas o número referente à disciplina.")
            return
        
        if self.banco.verificar_id(disciplina_add_falta):
            
            qtd_faltas = input("\nQuantas faltas deseja adicionar? (somente números): ")
                
            try:
                qtd_faltas = int(qtd_faltas)
                
            except:
                print("\nSelecione apenas números")
                return
            
            self.banco.atualizar_faltas(qtd_faltas, disciplina_add_falta)
            
            self.limpeza.limpar_terminal()
            print("\nFaltas adicionadas com sucesso!")
            return
            
        self.limpeza.limpar_terminal()
        print("\nMatéria não encontrada.")
        return
        

    
    def retirar_faltas(self):

        print("\nIndex - Disciplina / Faltas / Faltas Max")
        
        #SEGUIR O PASSO 3 DO GPT
        
        
        minhas_disciplinas = self.banco.listar_disciplinas("tudo")
        
        
        for i, d in enumerate(minhas_disciplinas):
            print(f"[{i}] - {d.nome} - {d.minhas_faltas} - {d.faltas_max}")

        disciplina_remove_falta = input("\nQual disciplina deseja retirar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            disciplina_remove_falta = int(disciplina_remove_falta)
            
        except:
            print("Digite apenas o número referente à disciplina.")
            return
        
        materia = minhas_disciplinas[disciplina_remove_falta]
        
        
        
            
        print(f"\nDisciplina selecionada: {materia.nome}")
        
        qtd_faltas = input("\nQuantas faltas deseja retirar? (somente números): ")
        
        try:
            qtd_faltas = int(qtd_faltas)
            
        except:
            print("\nSelecione apenas números")
            return
        
        novas_faltas = materia.minhas_faltas - qtd_faltas
        
        
        self.banco.atualizar_faltas(novas_faltas, materia.id)
        
        self.limpeza.limpar_terminal()
        print("\nFaltas retiradas com sucesso!")
        
        self.limpeza.limpar_terminal()
        print("\nMatéria não encontrada.")
        return

            
        