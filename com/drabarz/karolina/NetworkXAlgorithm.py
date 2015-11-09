import networkx as nx
from DominatingSetAlgorithm import DominatingSetAlgorithm

class NetworkXAlgorithm ( DominatingSetAlgorithm ):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "NXA"
        return dominatingSet;