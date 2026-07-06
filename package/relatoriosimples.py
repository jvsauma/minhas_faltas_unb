from package.relatorio import Relatorio

class RelatorioSimples(Relatorio):
    
    def __init__(self):
        pass
        
        
    
    def exibir_relatorio(self, lista):

        print("\n-----MINHA GRADE-----")
        print("\nMATÉRIAS / SUAS FALTAS")

        for materia in lista:

            print(
                f"\n{materia.nome} / "
                f"{materia.minhas_faltas}"
            )