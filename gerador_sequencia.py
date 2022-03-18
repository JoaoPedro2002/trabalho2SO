import numpy


class GeradorSequencia:

    def __init__(self, perfil: [], acessos_esperados: int):
        self.__perfil = perfil  # Exemplo: [(64 páginas dif, 16 de amplitude), (64, 8), (64, 4), (64, 2)]
        self.__acessos_esperados = acessos_esperados
        self.__acessos_realizados = 0
        self.__total_alocacoes = 0
        self.__paginas_ordenadas = []
        self.__paginas_embaralhadas = []

    @property
    def acessos_realizados(self):
        return self.__acessos_realizados

    @property
    def paginas_ordenadas(self):
        return self.__paginas_ordenadas

    @property
    def paginas_embaralhadas(self):
        return self.__paginas_embaralhadas

    def gera_sequencia_normal(self):
        for i in range(len(self.__perfil)):
            self.__total_alocacoes += self.__perfil[i][0] * self.__perfil[i][1]
        # print('Alocações básicas: ', self.__total_alocacoes)
        multiplicador = int(self.__acessos_esperados / self.__total_alocacoes)
        self.__acessos_realizados = multiplicador * self.__total_alocacoes

        pagina = 0
        for i in range(len(self.__perfil)):
            quantidade_paginas = self.__perfil[i][0]
            quantidade_alocacoes = self.__perfil[i][1] * multiplicador
            for k in range(quantidade_paginas):
                for j in range(quantidade_alocacoes):
                    self.__paginas_ordenadas.append(pagina)
                pagina += 1

    def gera_sequencia_embaralhada(self):
        paginas_ordenadas_array = numpy.array(self.__paginas_ordenadas)
        numpy.random.shuffle(paginas_ordenadas_array)
        # print(paginas_ordenadas_array)
        # print()

        self.__paginas_embaralhadas = paginas_ordenadas_array.tolist()
        # print(self.__paginas_embaralhadas)
        return self.__paginas_embaralhadas
