#-*- coding: utf-8 -*-
from operator import itemgetter, attrgetter, methodcaller
import numpy as np
import distutils
import sys
import os
import csv
import pandas as pd

# O parâmetro dirPart NECESSARIAMENTE tem que ser uma string
def loadCluster(dirPart, alg):
    """
    Função responsável pelo carregamento dos arquivos .clu gerados previamente
    em algoritmos de clusterização e pela geração de tabelas .tsv que serão
    carregadas pelo JavaScript para a visualização.
    Parâmetros
    ----------
        dirPart  :  string
            caminho do diretório com os arquivos .clu

        alg : int
            0 para o caso de ser chamado pelo upload de partições
            1 para o caso de geração de partições pelos algoritmos

    Retorno
    --------
        resDir  :   string
            string com o caminho do diretório com os arquivos
            - listIdenticalObjs.tsv
            - listDistinctClusters.tsv
            - result.tsv
            - objOrderEAC.tsv
    """

    print("LOAD CLUSTER {}".format(dirPart))
    merged = pd.DataFrame()
    clustersData = pd.DataFrame(columns=["ID", "cLabel", "pLabel"]) #pd.DataFrame(columns=["cID", "cLabel", "pLabel", "cSize"])

    clusterDir = dirPart
    (head, tail) = os.path.split(clusterDir);
    #(head, tail) = os.path.split(dirPart);


    print("head {}\ntail {}".format(head, tail))
    expUpload = tail;
    (lixo, expDirName) = os.path.split(head)

    # caso clustering
    if(alg == 1):
        print("expDirName {}".format(expDirName))
        resDir = "/var/www/cvis/static/resultados/" + expDirName
    # caso mocle
    elif(alg == 2):
        (lixo2, mocleExpDirName) = os.path.split(lixo)
        print("expDirName {}".format(expDirName))
        resDir = "/var/www/cvis/static/resultados/" + mocleExpDirName	
    # caso partitions
    else:
        print("expUpload {}".format(expUpload))
        resDir = "/var/www/cvis/static/resultados/" + expUpload		
    print("resDir {}".format(resDir))

    if not os.path.exists(resDir):
	#os.makedirs(resDir)
	try:
	    original_umask = os.umask(0)
            os.makedirs(resDir, 0777)
        finally:
            os.umask(original_umask)
 
    allClustersLabels = []
    print("clusterdir {}".format(clusterDir))
    for filename in os.listdir(clusterDir):
        file = clusterDir + '/' + filename
        p = pd.read_csv(file, sep="\t", header=None, encoding='utf-8', engine="python")
        p.columns = ["ID", "clusterLabel"]
        allClusters = set(p["clusterLabel"])

        for cluster in allClusters:
	    print(cluster)
            cLabel = "c"+str(cluster)
            newCluster = cLabel+filename
            allClustersLabels.insert(len(allClustersLabels), newCluster)
            p[newCluster] = (p["clusterLabel"] == cluster).astype(int) # column with cluster membership (1/0)
            clustersData = clustersData.append({"ID": newCluster, "cLabel": cLabel, "pLabel": filename, "cSize": p[newCluster].sum()}, ignore_index=True)
        del p["clusterLabel"]

        if merged.empty:
            merged = pd.DataFrame(p)
        else:
            merged = merged.merge(p, how="outer", on="ID")

    # identify groups of objects identically grouped and remove them from the dataset
    print(allClustersLabels)
    distinct = {}
    dist2 = merged.groupby(allClustersLabels, sort=False)
    file = resDir + '/listsIdenticalObjs.tsv'
    print(file)
    with open(file, 'w') as f:
        out = csv.writer(f, delimiter='\t', lineterminator='\n')
        # identify the objects identically grouped in all clusters
        for name, group in dist2:
            values = group["ID"].values
            distinct[values[0]] = values
            out.writerow(values)
    repeatedObjs = merged.loc[~merged["ID"].isin(distinct.keys())]["ID"].index
    # save the lists of identically grouped objects
    merged.drop(repeatedObjs,inplace=True)

    objectsIDs = merged["ID"]
    clustersData = clustersData.set_index(["ID"])
    merged = merged.set_index(["ID"])

    mergedT = merged.transpose()
    # identifies the distinct clusters
    distinctClusters = mergedT.drop_duplicates().index
    print("2")
    file = resDir + '/listDistinctClusters.tsv'
    with open(file, 'w') as f:
        out = csv.writer(f, delimiter='\t', lineterminator='\n')
        out.writerow([k for k in distinctClusters])
    complete = mergedT.join(clustersData)
    complete.sort_values(by=["cSize"], ascending=False, inplace=True)

    file = resDir + '/result.tsv'
    complete.to_csv(file ,sep='\t', index_label = "ID")
    eacM = {}

    for o1 in objectsIDs:
        eacM[o1] = complete.loc[complete[o1]==1]["cSize"].sum()

    x = sorted(eacM.items(), key=itemgetter(1), reverse=True)

    file = os.path.join(resDir, 'objOrderEAC.tsv')
    file = resDir + '/objOrderEAC.tsv'

    with open(file, 'w') as f:
        out = csv.writer(f, delimiter='\t', lineterminator='\n')
        out.writerow([k for (k,v) in x])

    return resDir
