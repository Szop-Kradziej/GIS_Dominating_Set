import networkx as nx
import copy

class ModifiedGreedyAlgorithm (object):
    def findDominatingSet(self, graph):
        print "MGA"
        
        modify_graph = copy.deepcopy(graph)
        dominating_set = []
        nodes = nx.nodes(modify_graph)
        
        while not len(nodes) == 0:
            node = self.findMaxDegreeNode(modify_graph)
            dominating_set.append(node)
            modify_graph = self.removeNodeAndNeighbors(modify_graph, node)
            nodes = nx.nodes(modify_graph)
            
        return dominating_set;
    
    def findMaxDegreeNode(self, graph):
        nodes = nx.nodes(graph)
        node = max(nodes, key=lambda node: nx.degree(graph, node))
        return node
    
    def removeNodeAndNeighbors(self, graph, node):
        new_graph = graph
        neighbors = new_graph.neighbors(node)
        node_in_neighbors = False
        
        if(node in neighbors):
            node_in_neighbors = True
        
        for neighbor in neighbors:
            if neighbor in new_graph:
                new_graph.remove_node(neighbor)
        
        if not node_in_neighbors:
            new_graph.remove_node(node)
        return new_graph