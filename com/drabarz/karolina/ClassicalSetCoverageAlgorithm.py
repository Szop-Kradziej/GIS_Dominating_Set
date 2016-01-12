import networkx as nx

class ClassicalSetCoverageAlgorithm (object):
    def findDominatingSet(self, graph):
        dominatingSet = nx.dominating_set(graph);
        print "CSCA"
        return dominatingSet;
    
    
        