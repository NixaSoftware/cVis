// Observacao: os r�tulos dos clusters s�o n�meros a partir de 1


// Class automatically generated by Dev-C++ New Class wizard

#ifndef PARTITION_H
#define PARTITION_H

#include <cstdio> 
#include <cstdlib> 
#include <string>
#include <iostream>
//#include <fstream> // usando a do boost
#include <map>
#include <set>
#include <iterator>

#include "clusteringTypes.h"

// para incluir as bibliotecas Boost
#include "boost/filesystem/operations.hpp" // includes boost/filesystem/path.hpp
#include "boost/filesystem/fstream.hpp"    // ditto
#include "boost/lexical_cast.hpp"

namespace fs = boost::filesystem;


//using std::string;
//using std::pair;
//using std::map;
//using std::iterator;
//using std::set;
//using namespace std;

//#define MAX_CLUSTERS    500

struct cmp
{
  bool operator()(std::string s1, std::string s2) const
  {
    return s1 < s2;
  }
};

// No description
class cpartition {

public:
    typedef std::pair <std::string, int> t_Pattern;
    typedef std::map<std::string, int, cmp> t_Patterns;
    typedef std::map<std::string, int, cmp>::iterator t_iterator_Patterns;

	// class constructor
	cpartition();
	cpartition(fs::path fileName);
	// class destructor
	//~partition();
	cpartition(const cpartition &part);
    cpartition &operator = (const cpartition &part);
	
private:     
    t_Patterns patterns;
    t_iterator_Patterns current;
    std::set<int> clustersLabels;

public:

    int nPatterns();
    int nClusters();
    t_iterator_Patterns currentPattern();
    t_iterator_Patterns first();
    t_iterator_Patterns last();
    t_iterator_Patterns find(std::string key);
    int loadPartition(fs::path);
    int printPartition(fs::path fileName); // grava o resultado do agrupamento em um arquivo
    int printPartition(); // mostra o resultado de um agrupamento na tela
    // generate a random partition with the clusters between 1 and k inclusive (k = number of clusters)
    int randomPartition(fs::path dataset, fs::path fileResult, int k); 
    std::set<int> getClustersLabels();
    t_Patterns getClustersPatterns();
    void patternInsert(std::string pat, int cluster);
    
};

#endif // PARTITION_H

