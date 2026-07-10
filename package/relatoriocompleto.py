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

            if materia.esta_reprovado():
                print("\nVocê reprovou por falta.")
            elif 0 < materia.faltas_restantes() <= 1:

                print(
                    f"\nATENÇÃO: Você ainda tem "
                    f"{materia.faltas_restantes()} falta(s)!"
                )