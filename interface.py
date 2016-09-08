# -*- coding: utf-8 -*-
# Organização de Arquivos Sequencial Indexada;
# Autores : Eliane, Lucas

from registro import *
from manipuladorArquivos import *
import sys

def pesq_binaria(chave, inicio, fim, pos, achou):
    """
    Pesquisa Binária pelo arquivo de indices.
    Parametros : chave é o código(String), inicio (Inicio do Arquivo Inteiro),
        fim (Final do arquivo), pos (Linha do Arquivo), Achou (Boolean)
    Return  posicao no arquivo de registros
    """
    if ((fim - inicio) > 0):
        meio = ((inicio+fim)/2)
        linha = lerLinhaIndice(meio, 0)
        if linha:
            atributos = linha.split(',')
            valor = atributos[0]
            posarq = atributos[1]
            if valor == chave:
                achou = True
                pos = posicao
                return posarq
            elif (valor > chave):
                return pesq_binaria(chave, inicio, meio, pos, achou)
            else:
                return pesq_binaria(chave, meio, fim, pos, achou)

def pesq_sequencial(linhachave, chave, indices, listaRegistros):
    """
    Pesquisa Sequencial pelo arquivo de indices.
    Parametros : linhachave String Linha do arquivo extencao para o elo,
        chave é o código(String), indices  Indice object(),
        listaRegistros Registros object()
    """
    ant = Registro( "", "", "", "", "")
    for i in indices.indices:
        if(chave > ant.codigo and chave < i.codigo):
            registro = listaRegistros.getRegistro(ant.codigo)
            registro.elo = linhachave
            indice = Indice(chave, ant.indice)
            indices.IncluiIndices(indice)
            indices.ordenarIndices()
            return
        ant = i

def gravaDados(linhaarq, registros, indices, numL):
    """
    Cria objetos, e adiciona a nas listas.
    Parametros : linhaarq String Linha do arquivo,
        registros Registros object(),
        indices  Indice object(),
        numL é a linha do arquivo para adicionar no indice,

    """
    registro = Registro(
        linhaarq[0:7], linhaarq[7:52], linhaarq[52:82],
        linhaarq[82:83], linhaarq[83:87]
    )
    registros.IncluiRegistros(registro)
    indice = Indice(linhaarq[0:7], numL)
    indices.IncluiIndices(indice)
    return

def gravaIndices(indices, linha):
    """
    Cria objetos Indices.
    Parametros : linha String Linha do arquivo,
        indices  Indice object(),
    """
    atributos = linha.split(",")
    codigo = atributos[0]
    ind = atributos[1]
    exc = atributos[2]
    indice = Indice(codigo, ind, exc)
    indices.IncluiIndices(indice)
    return

def incluiRegistroAreaExtencao(listaRegistrosExtensao, listaRegistros, listaIndices):
    """
    Inclui novos Registros na Area extencao.
    Parametros : listaRegistrosExtensao Registros object(),
        listaRegistros Registros object(),
        indices  Indice object(),
    """
    chave = (raw_input('\tDigite o codigo": '))
    nomeLivro = (raw_input('\tDigite o nome do Livro: '))
    nomeAutor = (raw_input('\tDigite o nome do Autor: '))
    mes = (raw_input('\tDigite o mes: '))
    ano = (raw_input('\tDigite o ano: '))
    registro = Registro(chave, nomeLivro, nomeAutor, mes, ano)
    listaRegistrosExtensao.IncluiRegistros(registro)
    pos = len(listaRegistrosExtensao.registros)
    pesq_sequencial(pos, chave, listaIndices, listaRegistros)
    return

def getRegistroArquivo(indices):
    """
    Faz busca do registro no arquivo de Indices e Retorna um registro.
    Parametros : Indices() object,
    Return : Retorna String de linha do Arquivo de DADOS
    """
    arq = open("arquivoIndices.txt", "w")
    chave = (raw_input('\tDigite o codigo que deseja buscar": '))
    arq.close()
    linha = ""
    if len(indices.indices):
        pos = pesq_binaria(chave, 0, len(indices.indices), 0, False)
        linha = lerLinha(pos, 0)
    return linha

def getExclusao(indices):
    """
    Faz busca do registro no arquivo de Indices.
    Parametros : Indices() object,
    Return : Retorna String de linha do Arquivo de DADOS
    """
    chave = (raw_input('\tDigite o codigo que deseja buscar": '))
    indice = indices.getIndice(chave)
    indice.excluirLogico()
    return

def main():
    """
    Inicio Sistema.
    Menu.
    """
    listaRegistros = Registros()
    listaExtencao = Registros()
    listaIndices = Indices()
    opcao = 5
    while opcao<=5:
        print "\n\tDigite 1 carregar arquivo de DADOS:\n"
        print "\tDigite 2 para pesquisar um registro:\n"
        print "\tDigite 3 para Inserir um novo registro\n"
        print "\tDigite 4 para Excluir um registro\n"

        opcao = int(raw_input('\tDigite a opcao: '))

        if(opcao == 1):
            lerArquivo(listaRegistros, listaIndices)
            listaIndices.ordenarIndices()
            gravarArquivoIndices(listaIndices)
        elif(opcao == 2):
            registro = getRegistroArquivo(listaIndices)
            print registro
        elif(opcao == 3):
            gravarArquivoIndices(listaIndices)
            gravarArquivoExtencao(listaExtencao)
            incluiRegistroAreaExtencao(listaExtencao, listaRegistros, listaIndices)
        elif(opcao == 4):
            getExclusao(listaIndices)

    gravarArquivoIndices(listaIndices)
    gravarArquivoExtencao(listaExtencao)
    return

if __name__ == '__main__':
    main()
