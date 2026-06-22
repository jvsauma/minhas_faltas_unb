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

        disciplinas = self.banco.listar_disciplinas("id")
        
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
        
        print("\nId - Disciplina / Horas / Faltas / Faltas Max")
        
        disciplinas = self.banco.listar_disciplinas("tudo")
        
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
            print("Digite apenas o número referente à disciplina.")
            return
        
        if self.banco.verificar_id(id_disciplina):
            
            qtd_faltas = input("\nQuantas faltas deseja adicionar? (somente números): ")
                
            try:
                qtd_faltas = int(qtd_faltas)
                
            except:
                print("\nSelecione apenas números")
                return
            
            
            materia = self.banco.verificar_id(id_disciplina)
            
            if not materia:
                return print("\nDisciplina não encontrada.")

            novas_faltas = (materia.minhas_faltas + qtd_faltas)

            self.banco.atualizar_faltas(
                novas_faltas,
                id_disciplina
            )
            
            
            self.limpeza.limpar_terminal()
            print("\nFaltas adicionadas com sucesso!")
            return
            
        self.limpeza.limpar_terminal()
        print("\nMatéria não encontrada.")
        return
        

    
    def retirar_faltas(self):

        print("\nId - Disciplina / Faltas / Faltas Max")
        
        disciplinas = self.banco.listar_disciplinas("tudo")
        
        
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
            return print("Digite apenas o número referente à disciplina.")

        if not self.banco.verificar_id(id_disciplina):
            return print("\nDisciplina não encontrada.")
            
        
            
        
        qtd_faltas = input("\nQuantas faltas deseja retirar? (somente números): ")
        
        try:
            qtd_faltas = int(qtd_faltas)
            
        except:
            return print("\nSelecione apenas números")
            
        
        
        materia = self.banco.verificar_id(id_disciplina)
        
        if not materia:
            return print("\nDisciplina não encontrada.")

        if materia.minhas_faltas < qtd_faltas:
            return print("\nNão é possível ficar com faltas negativas.")
        
        novas_faltas = (materia.minhas_faltas - qtd_faltas)

        self.banco.atualizar_faltas(novas_faltas, id_disciplina)
        
        
        self.limpeza.limpar_terminal()
        print("\nFaltas retiradas com sucesso!")

      
            
    def obter_disciplinas(self, flag):
        return self.banco.listar_disciplinas(flag)