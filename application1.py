"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
EX_GRAPH0 = {0: set([2,1]),
             1: set([]),
             2: set([])}

###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def compute_in_degrees(digraph):
    """function that takes the dictionary configuration of a directed graph
        and returns a dictionary with the same set of keys (nodes) as digraph 
        whose corresponding values are the 
        number of edges whose head matches a particular node."""
    result = dict([(x, 0) for x in digraph])
    for jdx in digraph.values():
        for kdx in jdx:
            result[kdx] += 1
    return result
        
def in_degree_distribution(digraph):
    """Takes a directed graph 'digraph' (as dictionary)
        and computes the unnormalized distribution of its in-degrees.
        Returns a dictionary whose keys correspond to in-degrees
        of nodes in the graph. The value associated with each 
        particular in-degree is the number of nodes with that in-degree."""
    in_degree_dictionary = compute_in_degrees(digraph)
    result = {}
    for idx in in_degree_dictionary.values():
        if idx in result.keys():
            result[idx] += 1
        else:
            result[idx] = 1
    return result

def in_degrees_dist_plot(in_degrees_dist, num_nodes):
    import matplotlib.pylab as plt
    x_axis = []
    y_axis = []
    for node, degree in in_degrees_dist.items():
        if node != 0:
            distribution = float(degree) / float(num_nodes)
            x_axis.append(node)
            y_axis.append(distribution)
    plt.loglog(x_axis, y_axis, 'ro')
    plt.xlabel('In-degrees')
    plt.ylabel('Distribution')
    plt.title('In degrees Distribution (log/log Plot)')
    plt.show()

citation_graph = load_graph(CITATION_URL)
#citation_graph = EX_GRAPH0
citation_graph_in_degree_distribution = in_degree_distribution(citation_graph)
c = 0
for i in citation_graph_in_degree_distribution.values():
	c += i
print c
citation_papers = 27770
#print citation_graph_in_degree_distribution
#in_degrees_dist_plot(citation_graph_in_degree_distribution, citation_papers)