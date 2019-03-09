

FILE = 'dijkstraData.txt'
REPORT_EDGES = ['7','37','59','82','99','115','133','165','188','197']

def read_graph():
    graph = {}
    edges = []
    with open(FILE, 'r') as f:
        for l in f.readlines():
            line = l.split()
            edge = line[0]
            edges.append(edge)
            graph[edge] = []
            graph[edge] = [x.split(',') for x in line[1:]]
    return graph, edges

def dijkstra(graph, edges, edge):

    X = {edge : 0}
    B = {}.fromkeys(edges)
    B[edge] = []

    while len(X) < len(edges):

        minVal = float('Inf')
        
        for origin in X.keys():
            for destiny in graph[origin]:
                if destiny[0] not in X.keys():
                    val = X[origin] + int(destiny[1])
                    if val < minVal:
                        edge_to_add = destiny[0]
                        minVal = val
                        path = B[origin] + [edge_to_add]

        X[edge_to_add] = minVal
        B[edge_to_add] = path

    return X, B
            
        
if __name__ == '__main__':
    
    graph, edges = read_graph()
    X, B = dijkstra(graph, edges, '1')
    results = [X[edge] for edge in REPORT_EDGES]
    
