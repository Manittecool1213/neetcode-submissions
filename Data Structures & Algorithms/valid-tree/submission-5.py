class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Cycle Detection:
        self.adjacency_list = {i : [] for i in range(n)}
        self.node_dict = {i : 0 for i in range(n)} # colour (0, 1, 2 : white, grey, black)
        for first, second in edges:
            self.adjacency_list[first].append(second)
            self.adjacency_list[second].append(first)
        
        def DFS_visit(node):
            self.node_dict[node] = 1
            for neighbour in self.adjacency_list[node]:
                if self.node_dict[neighbour] == 0:
                    self.node_dict[neighbour] = 1
                    if not DFS_visit(neighbour):
                        return False
                elif self.node_dict[neighbour] == 2:
                    return False
            self.node_dict[node] = 2
            return True

        for i in range(n):
            if self.node_dict[i] == 0:
                if not DFS_visit(i):
                    return False

        # Check on connectedness:
        dsu = DSU(n)
        for n1, n2 in edges:
            dsu.union(n1, n2)

        if max(dsu.size) != n:
            return False

        return True

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a 
            return True
        return False