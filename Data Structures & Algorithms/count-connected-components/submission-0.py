class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for n1, n2 in edges:
            dsu.union(n1, n2)

        return dsu.components
        
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.components -= 1
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a
            return True
        return False