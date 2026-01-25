class IMC:
    def __init__(self):
        self._classificacao = None #atributo privado para armazenar a classificacao
        
    def classificar(self, imc_valor):
        faixas = [ #lista com as faixas de classificacao
            (18.5, "MAGREZA"),
            (25, "NORMAL"),
            (30, "SOBREPESO"),
            (40, "OBESIDADE"),
            (float('inf'), "OBESIDADE GRAVE")
        ]
        for limite, classe in faixas:
            if imc_valor < limite:
                self._classificacao = classe
                break
        return self._classificacao
    
    def imprimir_classificacao(self):
        print(f"Sua Classificacao é: {self._classificacao}")
        