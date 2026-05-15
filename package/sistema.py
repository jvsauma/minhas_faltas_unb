from package.gerenciador import Gerenciador
from package.relatoriosimples import RelatorioSimples
from package.relatoriocompleto import RelatorioCompleto

class Sistema:
    def __init__(self):
        pass
        
        #resolver falta = nonetype
        
    def executar(self):
        self.rodando = True
        self.gerenciador = Gerenciador()

        
        while self.rodando:
            
            self.exibir_menu()
            
            escolha = input("Selecione uma opção: ")
            
            if escolha == "1":
                self.ver_faltas()
            elif escolha == "2":
                self.editar_faltas()
            elif escolha == "3":
                self.editar_disciplina()
            elif escolha == "4":
                self.sair()
            else:
                print("\nEscolha uma opção válida.\n")
            
            
    
    def exibir_menu(self):
        print("\n----- BEM VINDO A MINHA AGENDA UNB -----\n")
        print("\nÉ válido lembrar que:\nFaltou 2 horários (geralmente um dia de aula) = 2 faltas")
        print("""\nDigite o número equivalente para selecionar a opção:\n\n1- Ver faltas\n2- Editar faltas\n3- Editar disciplinas\n4- Sair do Gerenciador\n\n""")
        
    
    
    
    def ver_faltas(self):
        
        if not self.gerenciador.disciplinas:
            print("\nVocê ainda não possui disciplinas adicionadas.")
            
            return
        
        else:
            
            print("\nVocê dejesa:\n1- Relatório Simples\n2- Relatório Completo")
            escolha_relatorio = input("\nDigite aqui sua escolha (apenas números): ")
            
            try:
                escolha_relatorio = int(escolha_relatorio)
            except:
                print("\nDigite apenas números.")
                return
                
            
            if escolha_relatorio == 1:
                relatorio = RelatorioSimples()
                
                lista_ordenada_relatorio = self.gerenciador.criar_lista_ordenada()
                
                relatorio.exibir_relatorio(lista_ordenada_relatorio)
            
            elif escolha_relatorio == 2:
                relatorio = RelatorioCompleto()
                lista_ordenada_relatorio = self.gerenciador.criar_lista_ordenada()
                relatorio.exibir_relatorio(lista_ordenada_relatorio)
            
            else:
                print("\nDigite um número válido.")
            
            
    
    
    
    def editar_faltas(self):
        
        if not self.gerenciador.disciplinas:
            print("\nVocê ainda não possui disciplinas adicionadas.")
        
        else:
            print("\n-----MINHAS FALTAS-----")
            print("""\nVocê deseja:\n1- Adicionar falta\n2- Retirar falta\n3- Voltar para a tela inicial\n\n""")
            escolha = input("Selecione uma opção: ")
            
            if escolha == "1":
                
                self.gerenciador.lembrete()
                self.gerenciador.adicionar_faltas()
                
                pass
            
            elif escolha == "2":
                
                self.gerenciador.lembrete()
                self.gerenciador.retirar_faltas()
            
            elif escolha == "3":
                
                return
                
            
            else:
                
                print("\nEscolha uma opção válida.\n")
                self.editar_faltas()
            
        
        
    def editar_disciplina(self):
        
        print("\n-----DISCIPLINAS-----")
        print("""\nVocê deseja:\n1- Adicionar uma disciplina\n2- Remover uma disciplina\n3- Voltar para a tela inicial\n\n""")
        
        escolha = input("Selecione uma opção: ")
        
        if escolha == "1":
            
            self.gerenciador.lembrete()
            self.gerenciador.adicionar_disciplina()
    
        elif escolha == "2":
            
            self.gerenciador.lembrete()
            self.gerenciador.remover_disciplina()
            
        elif escolha == "3":
            
            return
            
        else:
            print("\nEscolha uma opção válida.\n")
            self.editar_disciplina()
            
        
        
    def sair(self):
        self.rodando = False