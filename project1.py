"""First project for Algorithmic Thinking"""

EX_GRAPH0 = {0: set([2,1]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([5,4,1]),
             1: set([6,2]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([5,4,1]),
             1: set([6,2]),
             2: set([7,3]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([2,1]),
             9: set([7,6,5,4,3,0])}


def make_complete_graph(num_nodes):
    """function that returns a complete graph
        with number of nodes = num_nodes"""
    result = {}
    for idx in range(0,num_nodes):
        result[idx] = set([])
        for jdx in range(0,num_nodes):
            if (idx!=jdx):
                result[idx].add(jdx)
    return result

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
        if idx in in_degree_dictionary.keys():
            in_degree_dictionary[idx] += 1
        else:
            in_degree_dictionary[idx] = 1
    return result





                
