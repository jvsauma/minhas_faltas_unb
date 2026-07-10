from package.disciplina import Disciplina
from package.banco_de_dados import BancoDeDados

class Gerenciador:
    def __init__(self):
        self.banco = BancoDeDados()

    def adicionar_disciplina(self, nome, horas):

        if self.banco.verificar_nome(nome):
            return False, "\nDisciplina já existente."

        if horas <= 0:
            return False, "\nA carga horária deve ser maior que zero."

        materia = Disciplina(nome, horas)
        max_faltas = materia.calcular_faltas(horas)
        self.banco.salvar_disciplina(nome, horas, 0, max_faltas)
        return True, "\nSua disciplina foi adicionada!"

    def remover_disciplina(self, disciplina_id):

        if not self.banco.verificar_tabela():
            return False, "\nNão existe disciplina para retirar."

        materia = self.banco.verificar_id(disciplina_id)
        if not materia:
            return False, "\nDisciplina não encontrada"

        self.banco.remover_disciplina(disciplina_id)
        return True, "\nDisciplina removida"

    def adicionar_faltas(self, disciplina_id, qtd_faltas):

        materia = self.banco.verificar_id(disciplina_id)

        if not materia:
            return False, "\nDisciplina não encontrada."

        if qtd_faltas <= 0:
            return False, "\nDigite um número maior que zero."

        materia.adicionar_faltas(qtd_faltas)
        self.banco.atualizar_faltas(materia.minhas_faltas, materia.id)
        return True, "\nFaltas adicionadas com sucesso"

    def retirar_faltas(self, disciplina_id, qtd_faltas):

        materia = self.banco.verificar_id(disciplina_id)

        if not materia:
            return False, "\nDisciplina não encontrada."

        if qtd_faltas <= 0:
            return False, "\nDigite um número maior que zero."

        if not materia.retirar_faltas(qtd_faltas):
            return False, "\nNão é possível ficar com falta negativas."

        self.banco.atualizar_faltas(materia.minhas_faltas, materia.id)
        return True, "\nFaltas retiradas com sucesso!"

    def inicializar(self):
        self.banco.conectar()
        self.banco.criar_tabela()

    def obter_disciplinas(self):
        return self.banco.listar_disciplinas()

    def encerrar(self):
        self.banco.fechar_conexao()

    def existem_disciplinas(self):
        return self.banco.verificar_tabela() is not None
