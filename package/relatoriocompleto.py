from package.relatorio import Relatorio

class RelatorioCompleto(Relatorio):
    
    def __init__(self):

        pass
        
    
    def exibir_relatorio(self, lista):

        print("\n-----MINHA GRADE-----")
        print("\nMATÉRIAS / HORAS / SUAS FALTAS / FALTAS MÁX")

        for materia in lista:

            print(
                f"\n{materia.nome} / "
                f"{materia.horas} / "
                f"{materia.minhas_faltas} / "
                f"{materia.faltas_max}"
            )

            if materia.minhas_faltas >= materia.faltas_max:
                print("\nVocê reprovou por falta.")

            elif abs(
                materia.minhas_faltas -
                materia.faltas_max
            ) <= 1:

                print(
                    f"\nATENÇÃO: Você ainda tem "
                    f"{abs(materia.minhas_faltas - materia.faltas_max)} falta(s)!"
                )