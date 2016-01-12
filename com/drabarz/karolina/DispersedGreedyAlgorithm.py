import networkx as nx

class DispersedGreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "DGA"
        return dominatingSet;