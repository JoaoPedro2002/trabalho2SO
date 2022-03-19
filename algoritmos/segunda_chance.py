from algoritmos.abstract_algoritmo import AlgoritmoAbstrato


class SegundaChance(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        self.__paginas_referenciadas = {}

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        self.__paginas_referenciadas[pagina] = True
        if pagina in self.__quadros_memoria:
            return

        self.__quantidade_page_faults += 1
        if len(self.__quadros_memoria) < self.__quantidade_quadros:
            self.__quadros_memoria.append(pagina)
        else:
            for i in range(self.__quantidade_quadros):
                dado = self.__quadros_memoria[i]
                if self.__paginas_referenciadas[dado]:
                    self.__quadros_memoria.pop(i)
                    self.__quadros_memoria.append(dado)
                    self.__paginas_referenciadas[dado] = False
                else:
                    self.__quadros_memoria.pop(i)
                    self.__quadros_memoria.append(pagina)
                    return
            self.__quadros_memoria.pop(0)
            self.__quadros_memoria.append(pagina)

    def clean(self):
        self.__quadros_memoria = []
        self.__quantidade_page_faults = 0
        self.__paginas_referenciadas = {}
