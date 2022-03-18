from algoritmos.abstract_algoritmo import AlgoritmoAbstrato


class LRU(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        for i in range(self.__quantidade_quadros):
            self.__quadros_memoria.append(None)

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        if pagina in self.__quadros_memoria:
            self.__quadros_memoria.remove(pagina)
            self.__quadros_memoria.insert(0, pagina)
            return
        for i in range(self.__quantidade_quadros):
            if self.__quadros_memoria[i] is None:
                self.__quadros_memoria[i] = pagina
                return
        self.__quantidade_page_faults += 1
        self.__quadros_memoria.pop()
        self.__quadros_memoria.insert(0, pagina)
