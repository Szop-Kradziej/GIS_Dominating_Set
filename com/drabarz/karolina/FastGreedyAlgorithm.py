import networkx as nx

class FastGreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        print "FGA"
        
        dominating_set = []
        sorted_nodes = self.getSortedNodes(graph)
        i = 1
        nodes = nx.nodes(graph)
        neighbor_sum_set = self.sumOfNeighbours(graph, i, sorted_nodes)
        while len(neighbor_sum_set) < len(nodes):
            node = sorted_nodes[i]
            if not self.isNodeNeighborsInSum(graph, node, neighbor_sum_set):
                dominating_set.append(node)
            i += 1
            neighbor_sum_set = self.sumOfNeighbours(graph,i, sorted_nodes)
        print sorted_nodes
        
        return dominating_set;
    
    def getSortedNodes(self, graph):
        nodes = nx.nodes(graph)
        sorted_nodes = sorted(nodes, key=lambda node: nx.degree(graph, node), reverse=False)
        sorted_nodes.reverse()
        return sorted_nodes
    
    def sumOfNeighbours(self, graph, i, sorted_nodes):
        sum = []
        
        for j in range(0, i - 1):
            node = sorted_nodes[j]
            neighbors = graph.neighbors(node)
            sum = self.addNeighborsToSum(sum, neighbors)
        return sum
    
    def addNeighborsToSum(self, sum, neighbors):
        new_sum = sum
        for neighbor in neighbors:
            if not neighbor in sum:
                new_sum.append(neighbor)
        return new_sum
            
    def isNodeNeighborsInSum(self, graph, node, sum):
        neighbors = graph.neighbors(node)
        for neighbor in neighbors :
            if not neighbor in sum :
                return False
        return True