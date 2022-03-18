import random


class GeradorSequencia:

    def __init__(self, perfil: [], numero_paginas: int):
        self.__perfil = perfil  # Exemplo: [(64 páginas dif, 16 de amplitude), (64, 8), (64, 4), (64, 2)]
        self.__numero_paginas = numero_paginas

    def _gera_sequencia_normal(self):
        alocacoes = sum(perfil[0] * perfil[1] for perfil in self.__perfil)
        multiplicador = int(self.__numero_paginas / alocacoes)
        paginas_ordenadas = []
        pagina = 0
        for item in self.__perfil:
            quantidade_paginas = item[0]
            quantidade_alocacoes = item[1] * multiplicador
            for k in range(quantidade_paginas):
                for j in range(quantidade_alocacoes):
                    paginas_ordenadas.append(pagina)
                pagina += 1
        return paginas_ordenadas

    def gera_sequencia_embaralhada(self):
        sequencia_embaralhada = self._gera_sequencia_normal()
        random.shuffle(sequencia_embaralhada)
        return sequencia_embaralhada
