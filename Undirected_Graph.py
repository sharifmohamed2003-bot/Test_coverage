import sys

class UndirectedGraph:
    def __init__(self, nodes=None, edges=None):
        self.graph = {}
        if nodes and edges is not None:
            self.build_undrirected(nodes, edges)
    def build_undrirected(self, nodes, edges):
        for nodes in nodes:
            self.graph[nodes] = []

        for edge in edges:
            n1, n2 = edge
            if n1 in self.graph and n2 in self.graph:
                self.graph[n1].append(n2)
                self.graph[n2].append(n1)
            
    def __str__(self):
        result = ""
        for node in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[node])
            result += node
            if neighbors:
                result += f" : {', '.join(neighbors)}"
            result += '\n'
        return result
    



nodes = input().strip().split()
edges = []
while True:
    try:
        edge_input = input().strip()
        if edge_input == "":
            break
        edge = tuple(edge_input.split())
        edges.append(edge)
    except EOFError:
        break
graph = UndirectedGraph(nodes, edges)
print(graph)