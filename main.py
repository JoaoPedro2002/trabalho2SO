from gerador_sequencia import GeradorSequencia
from algoritmos.fifo import FIFO
from algoritmos.lru import LRU
from algoritmos.nru import NRU
from algoritmos.segunda_chance import SegundaChance

# Define constantes
PAGINAS = 100000
QUADROS = 60
ITERACOES = 50

if __name__ == "__main__":
    # Teste 1: oferta 100.000 de páginas para 4 algoritmos e analisa page faults.
    gerador = GeradorSequencia(PAGINAS)  # gerador de sequencias de paginas
    # Inicializa algoritmos
    fifo = FIFO(QUADROS)
    segunda_chance = SegundaChance(QUADROS)
    nru = NRU(QUADROS, 1000, 10000)
    lru = LRU(QUADROS)

    resultados = {"paginas disitntas": 0, "FIFO": 0, "Segunda Chance": 0, "NRU": 0, "LRU": 0}

    print("  paginas distintas ", "  FIFO ", " Segunda Chance ", " NRU  ", "  LRU")
    for i in range(1, ITERACOES + 1):
        # Insere paginas aleatorias
        paginas_embaralhadas = gerador.gera_sequencia_embaralhada()
        for pagina in paginas_embaralhadas:
            fifo.insere_pagina(pagina)
            segunda_chance.insere_pagina(pagina)
            nru.insere_pagina(pagina)
            lru.insere_pagina(pagina)
        print("|       ", gerador.paginas_distintas, "       |",
              fifo.quantidade_page_faults, "|    ",
              segunda_chance.quantidade_page_faults, "    |",
              nru.quantidade_page_faults, "|",
              lru.quantidade_page_faults, "|")

        resultados["paginas disitntas"] += gerador.paginas_distintas
        resultados["FIFO"] += fifo.quantidade_page_faults
        resultados["Segunda Chance"] += segunda_chance.quantidade_page_faults
        resultados["NRU"] += nru.quantidade_page_faults
        resultados["LRU"] += lru.quantidade_page_faults

        # Limpa dados para a proxima iteracao
        fifo.clean()
        segunda_chance.clean()
        nru.clean()
        lru.clean()

    print('Media de paginas distintas: ', str(round(resultados["paginas disitntas"]/ITERACOES, 2)))
    print('Media de page faults (FIFO): ', str(round(resultados["FIFO"]/ITERACOES, 2)))
    print('Media de page faults (Segunda Chance): ', str(round(resultados["Segunda Chance"]/ITERACOES, 2)))
    print('Media de page faults (NRU): ', str(round(resultados["NRU"]/ITERACOES, 2)))
    print('Media de page faults (LRU): ', str(round(resultados["LRU"]/ITERACOES, 2)))
