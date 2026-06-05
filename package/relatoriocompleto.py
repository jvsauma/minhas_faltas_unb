from package.relatorio import Relatorio

class RelatorioCompleto(Relatorio):
    
    def __init__(self):

        pass
        
    
    def exibir_relatorio(self, lista):

        print("\n-----MINHA GRADE-----")
        print("\nMATÉRIAS / HORAS / SUAS FALTAS / FALTAS MÁX")

        for materia in lista:

            print(
                f"\n{materia[1]} / " #nome
                f"{materia[2]} / " #horas
                f"{materia[3]} / " #minhas faltas
                f"{materia[4]}" #faltas máxima
            )

            if materia[3] > materia[4]:
                print("\nVocê reprovou por falta.")

            elif materia[3] == materia[4]:
                print("\nVOCÊ NÃO PODE FALTAR MAIS!")

            elif abs(materia[3] - materia[4]) <= 2:
                print(
                    f"\nATENÇÃO: Você ainda tem "
                    f"{abs(materia[3] - materia[4])} falta(s)!"
                )