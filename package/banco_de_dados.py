import sqlite3
from package.disciplina import Disciplina

class BancoDeDados:
    
    def __init__(self):
        pass
    
    def conectar(self):
        self.conexao = sqlite3.connect("database/banco.db")
        self.cursor = self.conexao.cursor()
        
    
    def criar_tabela(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tabela_materias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    horas INTEGER NOT NULL,
    minhas_faltas INTEGER NOT NULL,
    faltas_max INTEGER NOT NULL
    )""")
        
        self.conexao.commit()
        
        
    def salvar_disciplina(self, nome, horas, minhas_faltas, faltas_max):
        
        self.cursor.execute("""INSERT INTO tabela_materias (nome, horas, minhas_faltas, faltas_max)
                            VALUES (?, ?, ?, ?)""", (nome, horas, minhas_faltas, faltas_max))
        
        self.conexao.commit()
        
        
    # NOVO: converte uma linha do banco em objeto Disciplina
    def _row_para_disciplina(self, row):

        if row is None:
            return None

        return Disciplina(row[1], row[2], row[3], row[4], id=row[0])
    
    # MODIFICADO
    def listar_disciplinas(self):

        self.cursor.execute(
            "SELECT * FROM tabela_materias"
        )

        disciplinas = self.cursor.fetchall()

        return [
            self._row_para_disciplina(materia)
            for materia in disciplinas
        ]
        
    
    def remover_disciplina(self, id):
        
        self.cursor.execute("""DELETE FROM tabela_materias
                            WHERE id = ?""", (id,))
        
        self.conexao.commit()
        
        
    
    def atualizar_faltas(self, minhas_faltas, id): #nome
        
        self.cursor.execute("""UPDATE tabela_materias
                            SET minhas_faltas = ?
                            WHERE id = ?""", (minhas_faltas, id))
        
        self.conexao.commit()
        
        
    # MODIFICADO
    def verificar_nome(self, nome):

        self.cursor.execute(
            """
            SELECT * FROM tabela_materias
            WHERE nome = ?
            """,
            (nome,)
        )

        resultado = self.cursor.fetchone()

        # ALTERADO
        return self._row_para_disciplina(resultado)
    
    
    # MODIFICADO
    def verificar_id(self, id):

        self.cursor.execute(
            """
            SELECT * FROM tabela_materias
            WHERE id = ?
            """,
            (id,)
        )

        resultado = self.cursor.fetchone()

        # ALTERADO
        return self._row_para_disciplina(resultado)
        
    
    def verificar_tabela(self):
        
        self.cursor.execute("SELECT * FROM tabela_materias")
        
        resultado = self.cursor.fetchone()
        
        return resultado
        
        
        
    def fechar_conexao(self):
        self.conexao.close()