from package.relatorio import Relatorio

class RelatorioSimples(Relatorio):
    
    def __init__(self):
        pass
        
        
    
    def exibir_relatorio(self, lista):
        
            
        print("\n-----MINHA GRADE-----")
        print("\nMATÉRIAS / SUAS FALTAS")
        
        #class relatorio - subclass relatorio simples e completo (polimorfismo e herança)
        
        for materia in lista:

            print(
                f"\n{materia[0]} / " #nome
                f"{materia[1]}" #minhas faltas
            )