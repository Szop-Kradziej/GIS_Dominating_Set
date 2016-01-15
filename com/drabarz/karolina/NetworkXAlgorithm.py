import networkx as nx
from DominatingSetAlgorithm import DominatingSetAlgorithm

class NetworkXAlgorithm ( DominatingSetAlgorithm ):
    def findDominatingSet(self, graph):
        print "Algorithm: NetworkX"
        dominating_set = nx.dominating_set(graph);
        dominating_set = list(dominating_set)
        return dominating_set;