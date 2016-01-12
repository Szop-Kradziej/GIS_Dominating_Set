import networkx as nx

class ClassicalSetCoverageAlgorithm (object):
    def findDominatingSet(self, graph):
        dominating_set = []
        print "CSCA"
        coverage_sets = self.getCoverageSets(graph)
        
        U = nx.nodes(graph)
        while not len(U) == 0:
            print U[0]
            max_covered_set = self.findMaxCoveredSet(U, coverage_sets)
            dominating_set = self.addSetToResult(dominating_set, max_covered_set)
            U = self.deleteNodes(U, max_covered_set)
        
        print len(coverage_sets)
        return dominating_set;
    
    def getCoverageSets(self, graph):
        coverage_sets = []
        nodes = nx.nodes(graph)
        for node in nodes:
            coverage_set = self.getCoverageSet(graph, node)
            coverage_sets.append(coverage_set)
        return coverage_sets
            
    def getCoverageSet(self, graph, node):
        neighbors = graph.neighbors(node)
        coverage_set = neighbors
        coverage_set.append(node)
        print coverage_set
        return coverage_set
    
    def findMaxCoveredSet(self, U, coverage_sets):
        max_covered_set = []
        print "findMaxCoveredSet"
        max_sum = 0
        for nodes_set in coverage_sets:
            sum = 0
            for node in nodes_set:
                if node in U:
                    sum += 1
            if sum > max_sum:
                max_sum = sum
                max_covered_set = nodes_set
            print "sum: ", sum, "max", max_sum
        return max_covered_set
    
    def addSetToResult(self, dominating_set, max_covered_set):
        new_dominating_set = dominating_set
        new_dominating_set.append(max_covered_set[-1])
       # for max_covered_node in max_covered_set:
           # if not max_covered_node in dominating_set:
          #      new_dominating_set.append(max_covered_node)
        return new_dominating_set
    
    def deleteNodes(self, U, max_covered_set):
        for max_covered_node in max_covered_set:
            if max_covered_node in U:
                U.remove(max_covered_node)
        return U
    
    
        