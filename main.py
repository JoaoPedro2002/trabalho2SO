from gerador_sequencia import GeradorSequencia
from algoritmos.fifo import FIFO
from algoritmos.lru import LRU
from algoritmos.nru import NRU
from algoritmos.segunda_chance import SegundaChance

PERFIL = [(25, 16), (25, 8), (25, 4), (25, 2)]
PAGINAS = 1000000
QUADROS = 60
ITERACOES = 50

if __name__ == "__main__":
    gerador = GeradorSequencia(PERFIL, PAGINAS)
    embaralhada = gerador.gera_sequencia_embaralhada()
    print("Total de páginas: ", PAGINAS)
    fifo = FIFO(QUADROS)
    relogio = SegundaChance(QUADROS)
    nru = NRU(QUADROS, 1000, 10000)
    lru = LRU(QUADROS)
    for pagina in embaralhada:
        fifo.insere_pagina(pagina)
        relogio.insere_pagina(pagina)
        nru.insere_pagina(pagina)
        lru.insere_pagina(pagina)
    print('Quantidade de page faults (FIFO): ', fifo.quantidade_page_faults)
    print('Quantidade de page faults (Relógio): ', relogio.quantidade_page_faults)
    print('Quantidade de page faults (NRU): ', nru.quantidade_page_faults)
    print('Quantidade de page faults (LRU): ', lru.quantidade_page_faults)

    # Teste 1: oferta 1.000.000 de páginas (perfil abaixo) para 4 algoritmos e analisa page faults.
    fifo = FIFO(QUADROS)
    relogio = SegundaChance(QUADROS)
    nru = NRU(QUADROS, 1000, 10000)
    lru = LRU(QUADROS)
    print("linha", " FIFO ", "  Segunda Chance  ", " NRU  ", "   LRU")
    for i in range(1, ITERACOES + 1):
        embaralhada = gerador.gera_sequencia_embaralhada()
        for pagina in embaralhada:
            fifo.insere_pagina(pagina)
            relogio.insere_pagina(pagina)
            nru.insere_pagina(pagina)
            lru.insere_pagina(pagina)
        print("|", i, "|",
              fifo.quantidade_page_faults, "|    ",
              relogio.quantidade_page_faults, "    |",
              nru.quantidade_page_faults, "|",
              lru.quantidade_page_faults, "|")
        fifo.clean()
        relogio.clean()
        nru.clean()
        lru.clean()
