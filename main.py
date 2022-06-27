import re
import networkx as nx
import pickle
import sys
import random

G = nx.Graph()

#function to build the nodes of the graph
def buildNodesOfGraph(G):

    with open("openthesaurus.txt") as rawdata:
        for index,line in enumerate(rawdata):
            if line.startswith('#'):
                continue
            else:
                cleanDataOfLine = re.sub(r"(.*?)\s?\(.*?\)", r"\1", line).lower()
                cleanDataOfLineWithoutSpaces = cleanDataOfLine.replace("\n", "")
                cleanDataOfLineWithoutSpaces = cleanDataOfLineWithoutSpaces.replace(" ", "")
                G.add_node(cleanDataOfLineWithoutSpaces)
    print("Nodes initialized")
    return

#functions to build the edges of the graph
def buildConnectionsOfGraph(G):

      for index, data in enumerate(list(G.nodes)):
            print(index/len(list(G.nodes)))
            listOfWordsOfPattern = data.split(";")
            for i in range(len(listOfWordsOfPattern)):
                for index2, data2 in enumerate(list(G.nodes)):
                    if (index2 != index):
                        listOfWordsOfPattern2 = data2.split(";")
                        for j in range(len(listOfWordsOfPattern2)):
                            if listOfWordsOfPattern[i] == listOfWordsOfPattern2[j]:
                                G.add_edge(data, data2, weight=listOfWordsOfPattern[i])
                            else:
                                continue
                    else:
                        continue

#set methods
def setGraphAsPickleObject(G, path):
    nx.write_gpickle(G, path)
    return 0

def setSubGraphAsPickle(subGraphs):

    object = subGraphs
    file = open('subgraphs2.obj', 'wb')
    pickle.dump(object, file)
    return 0

#get methods
def getGraphAsPickleObject(path):
    G = nx.read_gpickle(path)
    return G

def getSubGraphAsPickle():
    file = open("subgraphs.obj",'rb')
    subGraphs = pickle.load(file)
    return subGraphs

def getStrongSubGraphs(G, g, subGraphList, i):

    initialNode = list(G.nodes)[random.randint(0,len(list(G.nodes)))]
    shortestPathTree = nx.single_source_shortest_path_length(G, initialNode)

    subGraph = g.copy()
    cuttedOriginalGraph = G.copy()

    #get strong subgraph
    for nodeAsKey, distanceInGraph in shortestPathTree.items():
        for index, node in enumerate(list(subGraph.nodes)):
            if nodeAsKey != node:
                subGraph.remove_node(node)

    #get cutted graph without strong subgraph
    for nodeAsKey, distanceInGraph in shortestPathTree.items():
        for index, node in enumerate(list(cuttedOriginalGraph.nodes)):
            if nodeAsKey == node:
                cuttedOriginalGraph.remove_node(node)

    #print(list(subGraph))
    #print(list(subGraph.nodes))

    return subGraph

def getShortestPathInGraph(G, start, end):

    firstNode = []
    lastNode = []

    for index, data in enumerate(list(G.nodes)):
            listOfWordsOfPattern = data.split(";")
            for i in range(len(listOfWordsOfPattern)):
                if listOfWordsOfPattern[i] == start:
                    firstNode.append(data)
                if listOfWordsOfPattern[i] == end:
                    lastNode.append(data)

    selectNodeInList = 0
    print("Basic Information")
    print("start word is found in " + str(len(firstNode)) + " different word-patterns")
    print("end word is found in " + str(len(lastNode)) + " different word-patterns")
    print("Strting Node:")


    for i in range(len(firstNode)):
        for j in range(len(lastNode)):
            try:
                shortest_path = []
                try:
                    shortest_path = nx.shortest_path(G, firstNode[i], lastNode[j])
                except ValueError:
                    continue
                if len(shortest_path) != 0:
                    break
            except ValueError:
                continue

    print(start)
    print("Task:")
    print("Finde den kürzesten Weg zum Wort: " + str(end))
    NameOfChosenNode = start
    for i in range(len(shortest_path)):
            wordsOfActualNode = shortest_path[i].split(";")
            wordsOfActualNode = set(wordsOfActualNode)
            if i != (len(shortest_path)-1):
                wordsOfNextNode = shortest_path[i+1].split(";")
                wordsOfNextNode = set(wordsOfNextNode)
                if i == 0:
                    print(str(start) + " ist ein Synonym von " + str(list(set(wordsOfActualNode.intersection(wordsOfNextNode)))))
                else:
                    print('Das Wort '+ str(list(set(wordsOfActualNode.intersection(wordsOfNextNode)))).split("'")[1] + " ist ein Synonym des Wortes " + str(lastOne) + " in diesem neuen Kontext")
                print('Das Wort ' + str(list(set(wordsOfActualNode.intersection(wordsOfNextNode)))).split("'")[1] + ' im Kontext von ' + str(list(wordsOfActualNode)) + ' wird auch als ' +             str(list(set(wordsOfActualNode.intersection(wordsOfNextNode)))) + ' Im Kontext von ' + str(list(wordsOfNextNode))+ ' verwendet')
                lastOne = set(wordsOfActualNode.intersection(wordsOfNextNode))
            else:
                break

    print(str(lastOne) + " ist ein Synonym von " + str(end) + " im neu gewählten Kontext")
    print("Endknoten gefunden (" + str(end) + ")")

    return 0

if __name__ == "__main__":

    '''initalize graph'''
    #buildNodesOfGraph(G)
    #buildConnectionsOfGraph(G)
    #setGraphAsPickleObject(G, "graph.pickle")
    G = getGraphAsPickleObject("graph.pickle")

    '''analyze existence of strong subgraphs'''
    #subGraphList = []
    #i = 1
    #subGraphs = getStrongSubGraphs(G, subGraphList, i)

    #setSubGraphAsPickle(subGraphs)
    #print(len(subGraphList))
    #print(subGraphList)

    '''Examples:'''
    getShortestPathInGraph(G, 'blatt', 'fessel')
    #getShortestPathInGraph(G, 'blatt', 'idee')
    #getShortestPathInGraph(G, 'machen', 'tier')
    #getShortestPathInGraph(G, 'stuhl', 'hochzeit')
    #getShortestPathInGraph(G, 'schrank', 'auto')
    #getShortestPathInGraph(G, 'traktor', 'fabrik')
    #getShortestPathInGraph(G, 'unsicherheit', 'gewissheit')

    #components = nx.connected_components(G)
    #components = list(nx.connected_components(G))
    #largest_component = max(components, key=len)

