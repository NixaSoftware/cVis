#
# Script para criar as pastas necessárias e rodar os algoritmos de
# clusterização etc
#
import subprocess

def clustering(tipoDist, numObj, minK, maxK, dataset, expDir, alg):
    """
    Parâmetros:
    ----------
        tipoDist :  char
            E para distância Euclidiana
            P para correlação de Pearson
        numObj  :   int
            número de objetos
        minK    :   int
            número mínimo de clusters
            número máximo de clusters
        dataset :   string
            caminho absoluto para o arquivo com o dataset
        expDir  :   string
            caminho absoluto para o diretório com os resultados
        alg     :   int
            algoritmo de clusterização que será rodado
            1 - todos os algoritmos
            2 - SL
            3 - AL
            4 - CeL
            5 - CoL
            6 - SNN
            7 - KM
    Retorno:
    --------
        todos os arquivos .clu são gerados em subdiretórios, identificados pelo
        algoritmo selecionado, na pasta expDir
    """
<<<<<<< HEAD
    print("tipos clustering:\ntipoDist: {}\nnumObj: {}\nminK: {}\nmaxK: {}\ndataset: {}\nexpDir:{}\nalg: {}".format(type(tipoDist), type(numObj), type(minK), type(maxK), type(dataset), type(expDir), type(alg)))

    return subprocess.call(['./home/lasid/programs/clustering', tipoDist, int(numObj), int(minK), int(maxK), dataset, expDir, int(alg)])

def mocle(crossover, dataset, popIniDir, resultDir, truePartition):
    """
    Parâmetros
    ---------
        crossover  :  int
            1 - mcla
            2 - bipartite
        dataset    :  string
            caminho absoluto pro arquivo de dataset
        popIniDir  :  string
            caminho absoluto pro arquivo de população inicial
        resultDir  :  string
            caminho absoluto pro arquivo de resultados
        truePartition : fake
            é inútil
    """
    print("tipos:\ncrossover: {}\ndataset: {}\npopIniDir: {}\nresultDir: {}\n truePartition: {}".format(type(crossover), type(dataset), type(popIniDir), type(resultDir), type(truePartition)))

    return subprocess.call(['./home/lasid/programs/MOCLE-v3/mocle', int(crossover), dataset, popIniDir, resultDir, truePartition])
