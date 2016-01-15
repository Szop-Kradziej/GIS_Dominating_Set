import networkx as nx

class DominatingSetAlgorithm (object):
	def findDominatingSet(self, graph):
		dominating_set = nx.dominating_set(graph);
		print "DSA"
		return dominating_set;