import sys

class Queue:
    def __init__(self, size=3):
        self.A = [None] * size
        self.size = size
        self.head = -1
        self.tail = 0
        
    def is_empty(self):
        return self.head == -1
        
    def enqueue(self, x):
        if (self.tail + 1) % self.size == self.head:
            return "Queue Overflow"
        if self.is_empty():
            self.head = 0
        self.A[self.tail] = x
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        x = self.A[self.head]
        self.A[self.head] = None
        if self.head == (self.tail - 1) % self.size:
            self.head = -1
            self.tail = 0
        else:
            self.head = (self.head + 1) % self.size
        return x

    def search(self, x):
        if self.is_empty():
            return False
        i = self.head
        while True:
            if self.A[i] == x:
                return True
            i = (i + 1) % self.size
            if i == self.tail:
                break
        return False


class Stack:
    def __init__(self, size=100):
        self.A = [None] * size
        self.size = size
        self.top = -1
        
    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.top == self.size - 1:
            return "stack overflow"
        self.top += 1
        self.A[self.top] = item
        
    def pop(self):
        if self.is_empty():
            return "stack underflow"
        item = self.A[self.top]
        self.top -= 1
        return item
        
    def search(self, item):
        for i in range(self.top + 1):
            if self.A[i] == item:
                return i
        return -1


class UndirectedGraph:
    def __init__(self, nodes=None, edges=None):
        self.graph = {}
        if nodes and edges is not None:
            self.build_undirected(nodes, edges)

    def build_undirected(self, nodes, edges):
        for node in nodes:
            self.graph[node] = []
        for n1, n2 in edges:
            if n1 in self.graph and n2 in self.graph:
                self.graph[n1].append(n2)
                self.graph[n2].append(n1)

    def is_empty(self):
        return len(self.graph) == 0

    def BFS(self, start_node):
        if self.is_empty():
            return []
        visited = set([start_node])
        queue = [start_node]
        bfs_order = []
        while queue:
            current_node = queue.pop(0)
            bfs_order.append(current_node)
            for neighbor in sorted(self.graph[current_node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return bfs_order

    def DFS(self, start_node):
        if self.is_empty():
            return []
        visited = set()
        stack = Stack()
        stack.push(start_node)
        dfs_order = []
        while not stack.is_empty():
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                dfs_order.append(current_node)
                for neighbor in sorted(self.graph[current_node], reverse=True):
                    if neighbor not in visited:
                        stack.push(neighbor)
        return dfs_order

    def shortest_paths(self, s):
        paths = {s: [s]}
        queue = [s]
        while queue:
            node = queue.pop(0)
            for nei in self.graph[node]:
                if nei not in paths:
                    paths[nei] = paths[node] + [nei]
                    queue.append(nei)
        return paths

    def shortest_path_length(self, s, t):
        paths = self.shortest_paths(s)
        return paths[t] if t in paths else "unreachable"

    def __str__(self):
        result = ""
        for node in sorted(self.graph.keys()):
            neighbors = sorted(self.graph[node])
            line = node
            if neighbors:
                line += f" : {', '.join(neighbors)}"
            result += line + "\n"
        return result


graph = UndirectedGraph()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    cmd = parts[0]

    if cmd == "n":
        num_nodes = int(parts[1])
        nodes = parts[2 : 2 + num_nodes]
        remaining = parts[2 + num_nodes:]
        edges = []
        for i in range(0, len(remaining), 2):
            u = remaining[i]
            v = remaining[i + 1]
            edges.append((u, v))
        graph = UndirectedGraph(nodes, edges)
        print(graph, end="")

    elif cmd == "dfs":
        start = parts[1]
        result = graph.DFS(start)
        print(" ".join(result))

    elif cmd == "bfs":
        start = parts[1]
        result = graph.BFS(start)
        print(" ".join(result))

    elif cmd == "p":
        start = parts[1]
        paths = graph.shortest_paths(start)
        formatted = ", ".join(f"{node} : {len(paths[node])-1}" for node in sorted(paths.keys()))
        print(formatted)

    elif cmd == "d":
        s = parts[1]
        t = parts[2]
        path = graph.shortest_path_length(s, t)
        if path == "unreachable":
            print("No path")
        else:
            print(" ".join(path))
