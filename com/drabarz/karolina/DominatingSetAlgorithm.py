import networkx as nx

class DominatingSetAlgorithm (object):
	def findDominatingSet(self, graph):
		dominatingSet = nx.dominating_set(graph);
		print "DSA"
		return dominatingSet;