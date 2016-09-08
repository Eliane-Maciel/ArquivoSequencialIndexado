# -*- coding: utf-8 -*-

# Organização de Arquivos Sequencial Indexada;
# Autores : Eliane, Lucas

from registro import *
from interface import *
import sys

def lerArquivo(registros, indices):
    """
    LÊ arquivo de DADOS arquivo.txt.
    Parametros : Registros() object , Indices() object
    """
    arq = open("arquivo.txt", "r")
    numL = 0
    linha = arq.readline()
    gravaDados(linha, registros, indices, numL)
    numL = 0
    while linha:
        numL+=1
        linha = arq.readline()
        registro = gravaDados(linha, registros, indices, numL)

    arq.close()
    return

def lerLinha(pos, param):
    """
    param : Este é opcional e o padrão é 0, posicionamento arquivo absoluto,
    1 buscar em relação à posição atual,
    2 significa buscar em relação ao final do arquivo.
    pos : posicao no arquivo
    """
    arq = open("arquivo.txt", "r")
    linha = ""
    if pos and param:
        arq.seek(pos, param)
        linha = arq.readline()
    arq.close()
    return linha

def lerLinhaIndice(pos, param):
    """
    param : Este é opcional e o padrão é 0, posicionamento arquivo absoluto,
    1 buscar em relação à posição atual,
    2 significa buscar em relação ao final do arquivo.
    pos : posicao no arquivo
    """
    arq = open("arquivoIndices.txt", "r")
    arq.seek(pos, param)
    linha = arq.readline()
    arq.close()
    return linha

def lerArquivoIndices(indices):
    """
    LÊ arquivo de INDICES arquivoIndices.txt.
    Parametros : Indices() object
    """
    arq = open("arquivoIndices.txt", "r")
    linha = arq.readline()
    gravaIndices(indices, linha)
    while linha:
        linha = arq.readline()
        registro = gravaDados(indices, linha)

    arq.close()
    return

def gravarArquivoIndices(indices):
    """
    Grava objetos em formato texto no arquivo de Indices.
    Parametros : Indices() object,
    """
    arq = open("arquivoIndices.txt", "w")
    for i in indices.indices:
        linha = i.codigo + "," + str(i.indice) + "," + str(i.excluido) + "\n"
        arq.write(linha)
    arq.close()
    return

def gravarArquivoExtencao(listaRegistros):
    """
    Grava objetos em formato texto no arquivo Extencao
    Parametros : Registros() object,
    """
    arq = open("arquivoExtencao.txt", "w")
    for i in listaRegistros.registros:
        linha = i.codigo + i.nomeLivro + i.nomeAutor + i.mes + i.ano + "\n"
        arq.write(linha)
    arq.close()
    return
