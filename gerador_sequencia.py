import random


class GeradorSequencia:

    def __init__(self, numero_paginas: int):
        self.__numero_paginas = numero_paginas
        self.__paginas_distintas = None

    @property
    def paginas_distintas(self):
        return self.__paginas_distintas

    def _gera_sequencia_normal(self):
        sequencia = [(random.randint(25, 75), 2 ** random.randint(1, 4))
                     for _ in range(4)] # Define um padrao aleatoria da sequencia
        multiplicador = int(self.__numero_paginas / sum(perfil[0] * perfil[1] for perfil in sequencia))
        paginas_ordenadas = []
        pagina = 0
        for item in sequencia:
            quantidade_paginas = item[0]
            quantidade_alocacoes = item[1] * multiplicador
            for k in range(quantidade_paginas):
                for j in range(quantidade_alocacoes):
                    paginas_ordenadas.append(pagina)
                pagina += 1
        self.__paginas_distintas = pagina
        return paginas_ordenadas

    def gera_sequencia_embaralhada(self):
        sequencia_embaralhada = self._gera_sequencia_normal()
        random.shuffle(sequencia_embaralhada) # embaralha a lista
        return sequencia_embaralhada
