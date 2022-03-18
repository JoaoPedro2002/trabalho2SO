from algoritmos.abstract_algoritmo import AlgoritmoAbstrato


class SegundaChance(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        self.__pagina_referenciada = {}

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        self.__pagina_referenciada[pagina] = 1
        if pagina in self.__quadros_memoria:
            return
        if len(self.__quadros_memoria) < self.__quantidade_quadros:
            self.__quadros_memoria.append(pagina)
            return
        self.__quantidade_page_faults += 1
        contador = 0
        while contador < self.__quantidade_quadros:
            dado = self.__quadros_memoria[contador]
            if self.__pagina_referenciada[dado] == 1:
                self.__quadros_memoria.pop(contador)
                self.__quadros_memoria.append(dado)
                self.__pagina_referenciada[dado] = 0
            else:
                self.__quadros_memoria.pop(contador)
                self.__quadros_memoria.append(pagina)
                self.__pagina_referenciada[dado] = 0
                return
            contador += 1
        self.__quadros_memoria.pop(0)
        self.__quadros_memoria.append(pagina)

    def clean(self):
        self.__quadros_memoria = []
        self.__quantidade_page_faults = 0
        self.__pagina_referenciada = {}
