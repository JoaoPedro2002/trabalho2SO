from algoritmos.abstract_algoritmo import AlgoritmoAbstrato
import random


class NRU(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int, refresh_modificada, refresh_referenciada):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        self.__pagina_referenciada = {}
        self.__pagina_modificada = {}
        self.__contador_modificada = 0
        self.__contador_referenciada = 0
        self.__refresh_modificada = refresh_modificada
        self.__refresh_referenciada = refresh_referenciada

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        self.__contador_modificada += 1
        if self.__contador_modificada > self.__refresh_modificada:
            indice = random.randint(0, len(self.__quadros_memoria) - 1)
            pagina_aleatoria = self.__quadros_memoria[indice]
            self.__pagina_modificada[pagina_aleatoria] = 1
            self.__contador_modificada = 0
        else:
            self.__pagina_modificada[pagina] = 0

        self.__contador_referenciada += 1
        if self.__contador_referenciada > self.__refresh_referenciada:
            for pagina_em_quadro in self.__quadros_memoria:
                self.__pagina_referenciada[pagina_em_quadro] = 0
            self.__contador_referenciada = 0
        else:
            self.__pagina_referenciada[pagina] = 1

        if pagina in self.__quadros_memoria:
            return
        self.__quantidade_page_faults += 1
        if len(self.__quadros_memoria) < self.__quantidade_quadros:
            self.__quadros_memoria.append(pagina)
            return
        classe0 = []
        classe1 = []
        classe2 = []
        classe3 = []
        for i in range(self.__quantidade_quadros):
            dado = self.__quadros_memoria[i]
            if self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 0:
                classe0.append(dado)
            elif self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 1:
                classe1.append(dado)
            elif self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 0:
                classe2.append(dado)
            elif self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 1:
                classe3.append(dado)
        pagina_aleatoria = None
        if len(classe0) > 0:
            indice = random.randint(0, len(classe0) - 1)
            pagina_aleatoria = classe0[indice]
        elif len(classe1) > 0:
            indice = random.randint(0, len(classe1) - 1)
            pagina_aleatoria = classe1[indice]
        elif len(classe2) > 0:
            indice = random.randint(0, len(classe2) - 1)
            pagina_aleatoria = classe2[indice]
        elif len(classe3) > 0:
            indice = random.randint(0, len(classe3) - 1)
            pagina_aleatoria = classe3[indice]

        self.__quadros_memoria.remove(pagina_aleatoria)
        self.__quadros_memoria.append(pagina)
        self.__pagina_referenciada[pagina_aleatoria] = 0
        self.__pagina_modificada[pagina_aleatoria] = 0
        self.__pagina_referenciada[pagina] = 1
        self.__pagina_modificada[pagina] = 0

    def clean(self):
        self.__quadros_memoria = []
        self.__quantidade_page_faults = 0
        self.__pagina_referenciada = {}
        self.__pagina_modificada = {}
        self.__contador_modificada = 0
        self.__contador_modificada = 0
