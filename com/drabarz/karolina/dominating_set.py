import networkx as nx
import sys
import getopt
import csv 
import time
from com.drabarz.karolina.DominatingSetAlgorithm import DominatingSetAlgorithm
from com.drabarz.karolina.NetworkXAlgorithm import NetworkXAlgorithm
from com.drabarz.karolina.GreedyAlgorithm import GreedyAlgorithm
from com.drabarz.karolina.DispersedGreedyAlgorithm import DispersedGreedyAlgorithm
from com.drabarz.karolina.ClassicalSetCoverageAlgorithm import ClassicalSetCoverageAlgorithm
from com.drabarz.karolina.ModifiedGreedyAlgorithm import ModifiedGreedyAlgorithm
from com.drabarz.karolina.FastGreedyAlgorithm import FastGreedyAlgorithm

def getCommandLineArguments():
    argv = sys.argv[1:]
    graphFile = ''
    setFile = ''
    action = 'none'
    try:
        opts, args = getopt.getopt(argv,"hfcg:s:",["graphFile=","setFile="])
    except getopt.GetoptError:
        print 'test.py -g <graphFile> -s <setFile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'To find the smallest dominating set:'
            print '\ttest.py -f -g <graphFile> -s <setFile>'
            print 'To check if set is dominating:'
            print '\ttest.py -c -g <graphFile> -s <setFile>'
            sys.exit()
        elif opt == '-f' :
            action = "findDominatingSet"
        elif opt == '-c' :
            action = "checkIfSetIsDominating"
        elif opt in ("-g", "--graphFile"):
            graphFile = arg
        elif opt in ("-s", "--setFile"):
            setFile = arg
    print 'Graph file is "', graphFile
    print 'Set file is "', setFile
    return [graphFile, setFile, action];

def createGraphFromFile(graphFile):
    graph = nx.Graph();
    
    with open(graphFile, "rb") as inputfile:
        reader = csv.reader(inputfile);
        for i, line in enumerate(reader):
            if i < 4: continue
            edge = line[0].split('\t')
            graph.add_edge(edge[0], edge[1]);
    return graph;

def findAndShowDominatingSet(graph, setFile):
    algorithm = chooseAlgorithm();
    printGraphParamiters(graph);
    start_time = time.time()
    dominatingSet = algorithm.findDominatingSet(graph);
    stop_time = time.time() - start_time
    print "Algorithm execution time = %lf", stop_time
    printDominatingSet(dominatingSet);
    saveDominatingSet(dominatingSet, setFile);
    return;

def chooseAlgorithm():    
    while 1 :
        showMainMenu();
        answer = raw_input();
        if answer == '1' :
            return GreedyAlgorithm();
        elif answer == '2' :
            return DispersedGreedyAlgorithm();
        elif answer == '3' :
            return ClassicalSetCoverageAlgorithm();
        elif answer == '4' :
            return ModifiedGreedyAlgorithm();
        elif answer == '5' :
            return FastGreedyAlgorithm();
        elif answer == '6' :
            return NetworkXAlgorithm();
        sys.exc_clear();

def showMainMenu():
    print "Choose algorithm to calculate the smallest dominating set: "
    print "\t1) greedy algorithm"
    print "\t2) dispersed greedy algorithm"
    print "\t3) classical set coverage algorithm"
    print "\t4) modified greedy algorithm"
    print "\t5) fast greedy algorithm"
    print "\t6) use algorithm implemented in NetworkX library"
    return;

def printGraphParamiters(graph):
    print "Number of nodes: ", nx.number_of_nodes(graph);
    print "Number of edges: ", nx.number_of_edges(graph);
    return;

def printDominatingSet(dominatingSet):
    print "Number of nodes in dominating set: ", len(dominatingSet);
    for node in dominatingSet:
        print node;
    return;

def saveDominatingSet(dominatingSet, setFile):
    with open(setFile, 'wb') as outputFile:
        writer = csv.writer(outputFile);
        outputFile.write("#Number of nodes in dominating set: " + str(len(dominatingSet)) + "\n");
        for i in range(0, len(dominatingSet)):
            outputFile.write(str(dominatingSet[i])+ '\n')
    return;

def checkIfSetIsDominating(graph, setFile):
    inputSet = createSetFromFile(setFile);
    isDominatingSet = checkIfIsDominatingSet(graph, inputSet);
    print "Is set dominating: ", isDominatingSet;
    return;

def createSetFromFile(setFile):
    inputSet = set();
    
    with open(setFile, "rb") as inputfile:
        reader = csv.reader(inputfile);
        for i, line in enumerate(reader):
            if i < 1: continue
            node = line[0];
            inputSet.add(node);
    return inputSet;

def checkIfIsDominatingSet(graph, dominatingSet):
    return nx.is_dominating_set(graph, dominatingSet);

[graphFile, setFile, action] = getCommandLineArguments();
graph = createGraphFromFile(graphFile);

if action == "findDominatingSet" :
    findAndShowDominatingSet(graph, setFile);
elif action == "checkIfSetIsDominating" :
    checkIfSetIsDominating(graph, setFile);
else :
    sys.exit();