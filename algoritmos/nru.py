from algoritmos.abstract_algoritmo import AlgoritmoAbstrato
import random


class NRU(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int, refresh_modificada, refresh_r):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        self.__pagina_referenciada = {}
        self.__pagina_modificada = {}
        self.__contador_modificada = 0
        self.__contador_referenciada = 0
        self.__refresh_modificada = refresh_modificada
        self.__refresh_referenciada = refresh_r

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        """
        Neste ponto faz a simulação de escrita em memória (seta 1 bit M das páginas presentes em quadros)
        o zeramento periódico de todos os bits R.
        """
        self.__contador_modificada += 1
        if self.__contador_modificada > self.__refresh_modificada:
            indice = random.randint(1, len(self.__quadros_memoria)) - 1
            pagina_sorteada = self.__quadros_memoria[indice]
            self.__pagina_modificada[pagina_sorteada] = 1
            self.__contador_modificada = 0

        self.__contador_referenciada += 1
        if self.__contador_referenciada > self.__refresh_referenciada:
            for pagina_em_quadro in self.__quadros_memoria:
                self.__pagina_referenciada[pagina_em_quadro] = 0
            self.__contador_referenciada = 0

        self.__pagina_referenciada[pagina] = 1
        self.__pagina_modificada[pagina] = 0
        if pagina in self.__quadros_memoria:
            return
        self.__quantidade_page_faults += 1
        if len(self.__quadros_memoria) < self.__quantidade_quadros:
            self.__quadros_memoria.append(pagina)
            return

        # Separa as paginas em classes
        classe0 = []
        classe1 = []
        classe2 = []
        classe3 = []
        contador = 0
        while contador < self.__quantidade_quadros:
            dado = self.__quadros_memoria[contador]
            if self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 0:
                classe0.append(dado)
            elif self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 1:
                classe1.append(dado)
            elif self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 0:
                classe2.append(dado)
            elif self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 1:
                classe3.append(dado)
            contador += 1
        pagina_sorteada = None

        # remove uma pagina aleatoria da classe de menor numero
        if len(classe0) > 0:
            indice = random.randint(1, len(classe0)) - 1
            pagina_sorteada = classe0[indice]
        elif len(classe1) > 0:
            indice = random.randint(1, len(classe1)) - 1
            pagina_sorteada = classe1[indice]
        elif len(classe2) > 0:
            indice = random.randint(1, len(classe2)) - 1
            pagina_sorteada = classe2[indice]
        elif len(classe3) > 0:
            indice = random.randint(1, len(classe3)) - 1
            pagina_sorteada = classe3[indice]
        self.__quadros_memoria.remove(pagina_sorteada)
        self.__quadros_memoria.append(pagina)
        self.__pagina_referenciada[pagina_sorteada] = 0
        self.__pagina_modificada[pagina_sorteada] = 0
        self.__pagina_referenciada[pagina] = 1
        self.__pagina_modificada[pagina] = 0

    def clean(self):
        self.__quadros_memoria = []
        self.__quantidade_page_faults = 0
        self.__pagina_referenciada = {}
        self.__pagina_modificada = {}
        self.__contador_modificada = 0
        self.__contador_modificada = 0
