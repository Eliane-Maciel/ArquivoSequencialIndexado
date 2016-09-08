# -*- coding: utf-8 -*-

# Organização de Arquivos Sequencial Indexada;
# Autores : Eliane, Lucas

import operator

class Registro:
    """
    object Registro.
    """
    TAMANHOREGISTRO = 88;
    def __init__(self, codigo, nomeLivro, autor, mes, ano):
        # Inicializa as variaveis com os argumentos passados
        self.nomeAutor = autor
        self.mes = mes
        self.ano = ano
        self.codigo = codigo
        self.nomeLivro = nomeLivro
        self.elo = 0


class Registros:
    """
    Contém lista Registros.
    """
    # Contem os registros
    menorCodigo = 0

    def __init__(self):
        self.registros = []

    def IncluiRegistros(self, new_registros):
        # Recebe o registro passado
        self.registros.append(new_registros)

    def setRegistrosAt(self, registro, posicao):
        # Coloca o registro na posicao

        self.registros.insert(registro, posicao)

    def ordenarRegistros(self):
        # Ordena registros com pelo código
        self.registros.sort(key=operator.attrgetter('codigo'))

    def getRegistro(self, chave):
        # Retorna registro com a chave
        for i in self.registros:
            if(i.codigo == chave):
                return i

class Indice:
    """
    Object Indice.
    """
    def __init__(self, codigo, indice, excluido=False):
        # Inicializa as variaveis com os argumentos passados
        self.codigo = codigo
        self.excluido = excluido
        self.indice = indice

    def excluirLogico(self):
        self.excluido = True

class Indices:
    """
    Conjunto de Indices.
    """
    def __init__(self):
        # Inicializa as variaveis com os argumentos passados
        self.indices = []

    def IncluiIndices(self, new_indice):
        # Recebe o registro passado
        self.indices.append(new_indice)

    def setIndicesAt(self, indice, posicao):
        # Coloca o registro na posicao
        self.indices.insert(indice, posicao)

    def ordenarIndices(self):
        # Ordena Indices por código
        self.indices.sort(key=operator.attrgetter('codigo'))

    def getIndice(self, chave):
        # Retorna indice com a chave
        for i in self.indices:
            if(i.codigo == chave):
                return i
