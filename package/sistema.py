from package.gerenciador import Gerenciador

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
            print("\n-----MINHA GRADE-----")
            print("\nMATÉRIAS / HORAS / SUAS FALTAS / FALTAS MÁX")
            for i in self.gerenciador.disciplinas:
                print(f"\n{i.nome} / {i.horas} / {i.minhas_faltas} / {i.faltas_max}")
                
                if i.minhas_faltas > i.faltas_max:
                    print("\nVocê reprovou por falta.")
                
                elif i.minhas_faltas == i.faltas_max:
                    print("\nVOCÊ NÃO PODE FALTAR MAIS!")
                    
                elif abs(i.minhas_faltas - i.faltas_max) <= 2:
                    print(f"\nATENÇÃO: Você ainda tem {i.minhas_faltas - i.faltas_max} falta(s)!")
                
            pass
    
    
    
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
            self.gerenciador.remover_materia()
            
        elif escolha == "3":
            
            return
            
        else:
            print("\nEscolha uma opção válida.\n")
            self.editar_disciplina()
            
        
        
    def sair(self):
        self.rodando = False