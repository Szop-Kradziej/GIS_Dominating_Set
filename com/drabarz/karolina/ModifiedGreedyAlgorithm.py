import networkx as nx

class ModifiedGreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "MGA"
        return dominatingSet;