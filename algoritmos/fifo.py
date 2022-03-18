from algoritmos.abstract_algoritmo import AlgoritmoAbstrato


class FIFO(AlgoritmoAbstrato):

    def __init__(self, quantidade_quadros: int):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        if pagina in self.__quadros_memoria:
            return
        if len(self.__quadros_memoria) < self.__quantidade_quadros:
            self.__quadros_memoria.append(pagina)
            return
        self.__quantidade_page_faults += 1
        self.__quadros_memoria.pop(0)
        self.__quadros_memoria.append(pagina)

    def clean(self):
        self.__quadros_memoria = []
        self.__quantidade_page_faults = 0
