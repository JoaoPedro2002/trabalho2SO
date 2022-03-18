from gerador_sequencia import GeradorSequencia
from algoritmos.fifo import FIFO
from algoritmos.lru import LRU
from algoritmos.nru import NRU
from algoritmos.segunda_chance import SegundaChance

PERFIL = [(25, 16), (25, 8), (25, 4), (25, 2)]
PAGINAS = 100000
QUADROS = 60
ITERACOES = 50

if __name__ == "__main__":
    gerador = GeradorSequencia(PERFIL, PAGINAS)
    embaralhada = gerador.gera_sequencia_embaralhada()
    print("Total de páginas: ", PAGINAS)
    fifo = FIFO(QUADROS)
    segunda_chance = SegundaChance(QUADROS)
    nru = NRU(QUADROS, 1000, 10000)
    lru = LRU(QUADROS)
    for pagina in embaralhada:
        fifo.insere_pagina(pagina)
        segunda_chance.insere_pagina(pagina)
        nru.insere_pagina(pagina)
        lru.insere_pagina(pagina)
    print('Quantidade de page faults (FIFO): ', fifo.quantidade_page_faults)
    print('Quantidade de page faults (Segunda Chance): ', segunda_chance.quantidade_page_faults)
    print('Quantidade de page faults (NRU): ', nru.quantidade_page_faults)
    print('Quantidade de page faults (LRU): ', lru.quantidade_page_faults)

    # Teste 1: oferta 1.000.000 de páginas (perfil abaixo) para 4 algoritmos e analisa page faults.
    fifo = FIFO(QUADROS)
    segunda_chance = SegundaChance(QUADROS)
    nru = NRU(QUADROS, 1000, 10000)
    lru = LRU(QUADROS)

    resultados = {"FIFO": 0, "Segunda Chance": 0, "NRU": 0, "LRU": 0}

    print("linha", " FIFO ", "  Segunda Chance  ", " NRU  ", "   LRU")
    for i in range(1, ITERACOES + 1):
        embaralhada = gerador.gera_sequencia_embaralhada()
        for pagina in embaralhada:
            fifo.insere_pagina(pagina)
            segunda_chance.insere_pagina(pagina)
            nru.insere_pagina(pagina)
            lru.insere_pagina(pagina)
        print("|", i, "|",
              fifo.quantidade_page_faults, "|    ",
              segunda_chance.quantidade_page_faults, "    |",
              nru.quantidade_page_faults, "|",
              lru.quantidade_page_faults, "|")

        resultados["FIFO"] += fifo.quantidade_page_faults
        resultados["Segunda Chance"] += segunda_chance.quantidade_page_faults
        resultados["NRU"] += nru.quantidade_page_faults
        resultados["LRU"] += lru.quantidade_page_faults

        fifo.clean()
        segunda_chance.clean()
        nru.clean()
        lru.clean()

    print('Media de page faults (FIFO): ', str(round(resultados["FIFO"]/ITERACOES, 2)))
    print('Media de page faults (Segunda Chance): ', str(round(resultados["Segunda Chance"]/ITERACOES, 2)))
    print('Media de page faults (NRU): ', str(round(resultados["NRU"]/ITERACOES, 2)))
    print('Media de page faults (LRU): ', str(round(resultados["LRU"]/ITERACOES, 2)))
