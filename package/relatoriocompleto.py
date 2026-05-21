from package.relatorio import Relatorio

class RelatorioCompleto(Relatorio):
    
    def __init__(self):

        pass
        
    
    def exibir_relatorio(self, lista):

            
        print("\n-----MINHA GRADE-----")
        print("\nMATÉRIAS / HORAS / SUAS FALTAS / FALTAS MÁX")
        
        
        for dicionar in lista:
            print(f"\n{dicionar["nome"]} / {dicionar["horas"]} / {dicionar["minhas_faltas"]} / {dicionar["faltas_max"]}")
            
            if dicionar["minhas_faltas"] > dicionar["faltas_max"]:
                print("\nVocê reprovou por falta.")
            
            elif dicionar["minhas_faltas"] == dicionar["faltas_max"]:
                print("\nVOCÊ NÃO PODE FALTAR MAIS!")
                
            elif abs(dicionar["minhas_faltas"] - dicionar["faltas_max"]) <= 2:
                print(f"\nATENÇÃO: Você ainda tem {abs(dicionar["minhas_faltas"] - dicionar["faltas_max"])} falta(s)!")
            