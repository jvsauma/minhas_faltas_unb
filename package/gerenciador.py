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
        
        if horas <= 0:
            return print("\nA carga horária deve ser maior que zero.")
            
        
        
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

        disciplinas = self.banco.listar_disciplinas()
        
        print("")
        
        for materia in disciplinas:
            
            print(f"{materia.id} / {materia.nome}")

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
        
        disciplinas = self.banco.listar_disciplinas()
        
        if not disciplinas:
            self.limpeza.limpar_terminal()
            print("\nNão existem matérias cadastradas.")
            return
        
        print("\nId - Disciplina / Horas / Faltas / Faltas Max")
        
        
        for materia in disciplinas:
            print(
    f"{materia.id} / "
    f"{materia.nome} / "
    f"{materia.horas} / "
    f"{materia.minhas_faltas} / "
    f"{materia.faltas_max} \n"
)

        id_disciplina = input("\nQual disciplina deseja adicionar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            id_disciplina = int(id_disciplina)
            
        except:
            self.limpeza.limpar_terminal()
            print("Digite apenas números.")
            return
        
        materia = self.banco.verificar_id(id_disciplina)
        
        if not materia:
            
            print("\nDisciplina não encontrada.")
            return
            
        qtd_faltas = input("\nQuantas faltas deseja adicionar? (somente números): ")
                
        try:
            qtd_faltas = int(qtd_faltas)
            
        except:
            self.limpeza.limpar_terminal()
            print("\nDigite apenas números.")
            return
        
        if qtd_faltas <= 0:
            self.limpeza.limpar_terminal()
            print("\nDigite um número maior que zero.")
            return
    
        materia.adicionar_faltas(qtd_faltas)
        
        self.banco.atualizar_faltas(materia.minhas_faltas, materia.id)
            
        self.limpeza.limpar_terminal()
        print("\nFaltas adicionadas com sucesso")
        return
        

    
    def retirar_faltas(self):

        disciplinas = self.banco.listar_disciplinas()
        
        if not disciplinas:
            print("\nNão existem disciplinas cadastradas.")
            return
        
        print("\nId - Disciplina / Faltas / Faltas Max")
        
        
        for materia in disciplinas:
            print(
    f"{materia.id} / "
    f"{materia.nome} / "
    f"{materia.horas} / "
    f"{materia.minhas_faltas} / "
    f"{materia.faltas_max}\n"
)

        id_disciplina = input("\nQual disciplina deseja retirar a(s) falta(s)? (Digite o número referente): ").strip()
        
        try:
            id_disciplina = int(id_disciplina)

        except:
            self.limpeza.limpar_terminal()
            print("Digite apenas números.")
            return

        materia = self.banco.verificar_id(id_disciplina)
        
        if not materia:
            self.limpeza.limpar_terminal()
            print("\nDisciplina não encontrada.")
            return
        
        qtd_faltas = input("\nQuantas faltas deseja retirar? (somente números): ").strip()
        
        try:
            qtd_faltas = int(qtd_faltas)
            
        except:
            self.limpeza.limpar_terminal()
            return print("\nDigite apenas números")
            
        if qtd_faltas <= 0:
            self.limpeza.limpar_terminal()
            print("\nDigite um número maior que zero.")
            return
        
        # NOVO
        if not materia.retirar_faltas(qtd_faltas):
            self.limpeza.limpar_terminal()
            print("\nNão é possível ficar com falta negativas.")
            return
            
        self.banco.atualizar_faltas(materia.minhas_faltas, materia.id)
        
        self.limpeza.limpar_terminal()
        print("\nFaltas retiradas com sucesso!")

      
    #Banco de Dados
    def inicializar(self):
        self.banco.conectar()
        self.banco.criar_tabela()
        
    def obter_disciplinas(self):
        return self.banco.listar_disciplinas()
        
    def encerrar(self):
        self.banco.fechar_conexao()
        
    def existem_disciplinas(self):
        return self.banco.verificar_tabela() is not None