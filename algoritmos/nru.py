from algoritmos.abstract_algoritmo import AlgoritmoAbstrato
import random


class NRU(AlgoritmoAbstrato):
    def __init__(self, quantidade_quadros: int, refresh_m, refresh_r):
        self.__quantidade_page_faults = 0
        self.__quantidade_quadros = quantidade_quadros
        self.__quadros_memoria = []
        for i in range(self.__quantidade_quadros):
            self.__quadros_memoria.append(None)
        self.__pagina_referenciada = {}
        self.__pagina_modificada = {}
        self.__contador_incrementaM = 0
        self.__contador_zera_todosR = 0
        self.__refresh_m = refresh_m
        self.__refresh_r = refresh_r

    @property
    def quantidade_page_faults(self):
        return self.__quantidade_page_faults

    def insere_pagina(self, pagina):
        """
        Neste ponto faz a simulação de escrita em memória (seta 1 bit M das páginas presentes em quadros)
        o zeramento periódico de todos os bits R.
        """
        self.__contador_incrementaM += 1
        if self.__contador_incrementaM > self.__refresh_m:
            indice = random.randint(1, len(self.__quadros_memoria)) - 1
            pagina_sorteada = self.__quadros_memoria[indice]
            self.__pagina_modificada[pagina_sorteada] = 1
            self.__contador_incrementaM = 0

        self.__contador_zera_todosR += 1
        if self.__contador_zera_todosR > self.__refresh_r:
            for paginas in self.__quadros_memoria:
                self.__pagina_referenciada[paginas] = 0
            self.__contador_zera_todosR = 0

        self.__pagina_referenciada[pagina] = 1
        self.__pagina_modificada[pagina] = 0
        if pagina in self.__quadros_memoria:
            return
        for i in range(self.__quantidade_quadros):
            if self.__quadros_memoria[i] is None:
                self.__quadros_memoria[i] = pagina
                return
        self.__quantidade_page_faults += 1
        classe0 = []
        classe1 = []
        classe2 = []
        classe3 = []
        contador = 0
        while contador < self.__quantidade_quadros:
            dado = self.__quadros_memoria[contador]
            if self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 0:
                classe0.append(dado)
            else:
                if self.__pagina_referenciada[dado] == 0 and self.__pagina_modificada[dado] == 1:
                    classe1.append(dado)
                else:
                    if self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 0:
                        classe2.append(dado)
                    else:
                        if self.__pagina_referenciada[dado] == 1 and self.__pagina_modificada[dado] == 1:
                            classe3.append(dado)
            contador += 1
        pagina_sorteada = None
        if len(classe0) > 0:
            indice = random.randint(1, len(classe0)) - 1
            pagina_sorteada = classe0[indice]
        else:
            if len(classe1) > 0:
                indice = random.randint(1, len(classe1)) - 1
                pagina_sorteada = classe1[indice]
            else:
                if len(classe2) > 0:
                    indice = random.randint(1, len(classe2)) - 1
                    pagina_sorteada = classe2[indice]
                else:
                    if len(classe3) > 0:
                        indice = random.randint(1, len(classe3)) - 1
                        pagina_sorteada = classe3[indice]
        self.__quadros_memoria.remove(pagina_sorteada)
        self.__quadros_memoria.append(pagina)
        self.__pagina_referenciada[pagina_sorteada] = 0
        self.__pagina_modificada[pagina_sorteada] = 0
        self.__pagina_referenciada[pagina] = 1
        self.__pagina_modificada[pagina] = 0
