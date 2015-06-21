"""project 2 for algorithmic thinking"""

import poc_queue
import random
#import alg_module2_graphs as samples

def bfs_visited(ugraph, start_node):
    """Implementation of bfs_visited algorithm"""
    my_q = poc_queue.Queue()
    visited = set([start_node])
    my_q.enqueue(start_node)
    size = 1
    while size!=0 :
        curr = my_q.dequeue()
        size -= 1
        for neighbour in ugraph[curr]:
            if neighbour not in visited:
                visited = visited.union(set([neighbour]))
                my_q.enqueue(neighbour)
                size += 1
    return visited
    
def cc_visited(ugraph):
    """Implementation of cc_visited algorithm"""
    remaining_nodes = set(ugraph.keys())
    connected_comps = []
    while len(remaining_nodes)!=0:
        arb = random.choice(tuple(remaining_nodes))
        comp = bfs_visited(ugraph,arb)
        connected_comps.append(set(comp))
        remaining_nodes = remaining_nodes.difference(comp)
    return list(connected_comps)

def largest_cc_size(ugraph):
    """Implementation of largest_cc_size"""
    connected_comps = cc_visited(ugraph)
    max_size = 0
    for item in connected_comps:
        if len(item) > max_size:
            max_size = len(item)
    return max_size

def compute_resilience(ugraph, attack_order):
    """Implementation of compute resilience"""
    result = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node,None)
        for neighbours in ugraph.values():
            if node in neighbours:
                neighbours.remove(node)
        result.append(largest_cc_size(ugraph))
    return result
        

#compute_resilience(samples.GRAPH0, [0,1])