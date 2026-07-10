from package.gerenciador import Gerenciador
from package.limpeza import Limpeza
from package.relatoriosimples import RelatorioSimples
from package.relatoriocompleto import RelatorioCompleto

class Sistema:
    def __init__(self):
        pass

    def executar(self):
        self.rodando = True
        self.gerenciador = Gerenciador()
        self.limpeza = Limpeza()
        self.gerenciador.inicializar()

        while self.rodando:
            self.exibir_menu()
            escolha = input("Selecione uma opção: ")

            if escolha == "1":
                self.limpeza.limpar_terminal()
                self.ver_faltas()
            elif escolha == "2":
                self.limpeza.limpar_terminal()
                self.editar_faltas()
            elif escolha == "3":
                self.limpeza.limpar_terminal()
                self.editar_disciplina()
            elif escolha == "4":
                self.sair()
            else:
                self.limpeza.limpar_terminal()
                print("\nEscolha uma opção válida.\n")

    def exibir_menu(self):
        print("\n----- BEM VINDO A MINHA AGENDA UNB -----\n")
        print("\nÉ válido lembrar que:\nFaltou 2 horários (geralmente um dia de aula) = 2 faltas")
        print("""\nDigite o número equivalente para selecionar a opção:\n\n1- Ver faltas\n2- Editar faltas\n3- Editar disciplinas\n4- Sair do Gerenciador\n\n""")

    def exibir_lembrete(self):

        print("\nLEMBRANDO: Escreva o nome da matéria exatamente como ela está registrada.")

    def ver_faltas(self):
        if not self.gerenciador.existem_disciplinas():
            print("\nVocê ainda não possui disciplinas adicionadas.")
            return

        print("\nVocê dejesa:\n1- Relatório Simples\n2- Relatório Completo")
        escolha_relatorio = input("\nDigite aqui sua escolha (apenas números): ")

        try:
            escolha_relatorio = int(escolha_relatorio)
        except:
            print("\nDigite apenas números.")
            return

        disciplinas = self.gerenciador.obter_disciplinas()
        self.limpeza.limpar_terminal()

        if escolha_relatorio == 1:
            relatorio = RelatorioSimples()
            relatorio.exibir_relatorio(disciplinas)
        elif escolha_relatorio == 2:
            relatorio = RelatorioCompleto()
            relatorio.exibir_relatorio(disciplinas)
        else:
            print("\nDigite um número válido.")

    def editar_faltas(self):
        if not self.gerenciador.existem_disciplinas():
            print("\nVocê ainda não possui disciplinas adicionadas.")
            return

        print("\n-----MINHAS FALTAS-----")
        print("""\nVocê deseja:\n1- Adicionar falta\n2- Retirar falta\n3- Voltar para a tela inicial\n\n""")
        escolha = input("Selecione uma opção: ")

        if escolha == "1":
            self.limpeza.limpar_terminal()
            self.exibir_lembrete()
            self.adicionar_faltas_interface()
        elif escolha == "2":
            self.limpeza.limpar_terminal()
            self.exibir_lembrete()
            self.retirar_faltas_interface()
        elif escolha == "3":
            self.limpeza.limpar_terminal()
            return
        else:
            self.limpeza.limpar_terminal()
            print("\nEscolha uma opção válida.\n")
            self.editar_faltas()

    def adicionar_faltas_interface(self):
        disciplinas = self.gerenciador.obter_disciplinas()

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

        qtd_faltas = input("\nQuantas faltas deseja adicionar? (somente números): ")
        try:
            qtd_faltas = int(qtd_faltas)
        except:
            self.limpeza.limpar_terminal()
            print("\nDigite apenas números.")
            return

        sucesso, mensagem = self.gerenciador.adicionar_faltas(id_disciplina, qtd_faltas)
        self.limpeza.limpar_terminal()
        print(mensagem)

    def retirar_faltas_interface(self):
        disciplinas = self.gerenciador.obter_disciplinas()

        print("\nId - Disciplina / Horas / Faltas / Faltas Max")
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

        qtd_faltas = input("\nQuantas faltas deseja retirar? (somente números): ").strip()
        try:
            qtd_faltas = int(qtd_faltas)
        except:
            self.limpeza.limpar_terminal()
            print("\nDigite apenas números")
            return

        sucesso, mensagem = self.gerenciador.retirar_faltas(id_disciplina, qtd_faltas)
        self.limpeza.limpar_terminal()
        print(mensagem)

    def editar_disciplina(self):
        print("\n-----DISCIPLINAS-----")
        print("""\nVocê deseja:\n1- Adicionar uma disciplina\n2- Remover uma disciplina\n3- Voltar para a tela inicial\n\n""")

        escolha = input("Selecione uma opção: ")

        if escolha == "1":
            self.limpeza.limpar_terminal()
            self.exibir_lembrete()
            self.adicionar_disciplina_interface()
        elif escolha == "2":
            self.limpeza.limpar_terminal()
            self.exibir_lembrete()
            self.remover_disciplina_interface()
        elif escolha == "3":
            self.limpeza.limpar_terminal()
            return
        else:
            self.limpeza.limpar_terminal()
            print("\nEscolha uma opção válida.\n")
            self.editar_disciplina()

    def adicionar_disciplina_interface(self):
        nome = input("\nDigite o nome da disciplina: ").strip()
        horas = input("\nDigite as horas da disciplina (somente números): ").strip()

        try:
            horas = int(horas)
        except:
            self.limpeza.limpar_terminal()
            print("\nSó é permitido números.")
            return

        sucesso, mensagem = self.gerenciador.adicionar_disciplina(nome, horas)
        self.limpeza.limpar_terminal()
        print(mensagem)

    def remover_disciplina_interface(self):
        disciplinas = self.gerenciador.obter_disciplinas()

        if not disciplinas:
            self.limpeza.limpar_terminal()
            print("\nNão existe disciplina para retirar.")
            return

        print("\nId - Disciplina")
        for materia in disciplinas:
            print(f"{materia.id} / {materia.nome}")

        disciplina_remove_disciplina = input("\nQual disciplina você deseja remover? (Digite o id referente): ").strip()
        try:
            disciplina_remove_disciplina = int(disciplina_remove_disciplina)
        except:
            self.limpeza.limpar_terminal()
            print("Digite somente números")
            return

        sucesso, mensagem = self.gerenciador.remover_disciplina(disciplina_remove_disciplina)
        self.limpeza.limpar_terminal()
        print(mensagem)

    def sair(self):
        self.gerenciador.encerrar()
        self.rodando = False
