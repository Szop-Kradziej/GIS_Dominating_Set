import networkx as nx

class GreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "GA"
        return dominatingSet;
