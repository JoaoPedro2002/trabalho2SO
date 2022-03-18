from abc import ABC, abstractmethod


class AlgoritmoAbstrato(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def quantidade_page_faults(self):
        pass

    @abstractmethod
    def insere_pagina(self, pagina):
        pass

    @abstractmethod
    def clean(self):
        pass
