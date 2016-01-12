import networkx as nx

class FastGreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "FGA"
        return dominatingSet;