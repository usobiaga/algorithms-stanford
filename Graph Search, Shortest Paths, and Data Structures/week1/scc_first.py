import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

FILE = 'scc.txt'


def read_graph():
    graph = {}
    with open(FILE, 'r') as f:
        for l in f.readlines():
            line = l.split()
            if (line[0] in graph):
                graph[line[0]].append(line[1])
            else:
                graph[line[0]] = [line[1]]
    
    allvals = set(flatten(graph.values()))
    for val in allvals:
        if val not in graph.keys():
            graph[val] = []
    return graph



def read_graph_reversed():
    graph = {}
    with open(FILE, 'r') as f:
        for l in f.readlines():
            line = l.split()
            if (line[1] in graph):
                graph[line[1]].append(line[0])
            else:
                graph[line[1]] = [line[0]]

    allvals = set(flatten(graph.values()))
    for val in allvals:
        if val not in graph.keys():
            graph[val] = []

    return graph



def flatten(alist):
    return [item for sublist in alist for item in sublist]


def relabel_graph(graph, edge_order):
    new_graph = {}
    for key in graph:
        new_graph[edge_order[key]] = []
        for edge in graph[key]:
            new_graph[edge_order[key]].append(edge_order[edge])
    return new_graph
                

def dfs_loop(graph, ordered):

    def dfs(graph, node_i):
        nonlocal tval
        explored[node_i] = True

        if ordered: leaders[node_i] = leader

        for node_j in graph[node_i]:
            if explored[node_j] is None:
                dfs(graph, node_j)

        if not ordered:
            tval += 1
            t[node_i] = str(tval)
            
    
    edges = set(graph.keys()) | set(flatten(graph.values()))
    explored = {}.fromkeys(edges)
    
    if not ordered:
        t = explored.copy()
        tval = 0
    else :
        leaders = explored.copy()

    keys_decreasing = sorted(graph.keys(), reverse = True)
    for i in keys_decreasing:
        if explored[i] is None:
            leader = i
            dfs(graph, i)

    if not ordered:
        return t
    else:
        return leaders
    

def computeSCCs():
    
    graph = read_graph()
    graph_reversed = read_graph_reversed()

    edge_order = dfs_loop(graph_reversed, False)
    graph_relabeled = relabel_graph(graph, edge_order)
    leaders = dfs_loop(graph_relabeled, True)
    unique_leaders = list(set(leaders.values()))
    
    count = {}.fromkeys(unique_leaders, 0)
    for leader in leaders.values():
        count[leader] = count[leader] + 1
    
    print(sorted(count.values(), reverse = True)[:5])

    
if __name__ == '__main__':

    thread = threading.Thread(target = computeSCCs)
    thread.start()

