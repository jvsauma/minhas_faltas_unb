import sqlite3

class BancoDeDados:
    
    def __init__(self):
        pass
    
    def conectar(self):
        self.conexao = sqlite3.connect("banco.db")
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
        
    
    def listar_disciplinas(self, flag):
        
        if flag == "tudo":
            
            self.cursor.execute("SELECT * FROM tabela_materias")
            
        elif flag == "nome_minhas_faltas":
            
            self.cursor.execute("SELECT nome, minhas_faltas FROM tabela_materias")
            
        elif flag == "sem_id":
            
            self.cursor.execute("SELECT nome, horas, minhas_faltas, faltas_max FROM tabela_materias")
        
        elif flag == "id":
            
            self.cursor.execute("SELECT id, nome FROM tabela_materias")
            
            
        disciplinas = self.cursor.fetchall()
        
        return disciplinas
        
    
    def remover_disciplina(self, id):
        
        self.cursor.execute("""DELETE FROM tabela_materias
                            WHERE id = ?""", (id,))
        
        self.conexao.commit()
        
        
    
    def atualizar_faltas(self, minhas_faltas, id): #nome
        
        self.cursor.execute("""UPDATE tabela_materias
                            SET minhas_faltas = ?
                            WHERE id = ?""", (minhas_faltas, id))
        
        self.conexao.commit()
        
        
    def verificar_nome(self, nome):
        
        #retorna true ou false
        self.cursor.execute("""SELECT * FROM tabela_materias
                            WHERE nome = ?""", (nome,))
        
        resultado = self.cursor.fetchone()
        
        return resultado
    
    
    def verificar_id(self, id):
        
        #retorna true ou false
        self.cursor.execute("""SELECT * FROM tabela_materias
                            WHERE id = ?""", (id,))
        
        resultado = self.cursor.fetchone()
        
        return resultado
        
    
    def verificar_tabela(self):
        
        self.cursor.execute("SELECT * FROM tabela_materias")
        
        resultado = self.cursor.fetchone()
        
        return resultado
        
        
        
    def fechar_conexao(self):
        self.conexao.close()