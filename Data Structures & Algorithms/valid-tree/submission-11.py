class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for e1, e2 in edges:
            if not dsu.union(e1, e2):
                return False

        if dsu.components != 1:
            return False

        return True
    
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a
            self.components -= 1
            return True
        return False