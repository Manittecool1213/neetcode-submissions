class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        self.visited = 0
        self.adjacency_list = {i : [] for i in range(n)}
        self.node_dict = {i : 0 for i in range(n)} # colour (0, 1, 2 : white, grey, black)
        for first, second in edges:
            self.adjacency_list[first].append(second)
            self.adjacency_list[second].append(first)

        def DFS_visit(node):
            self.visited += 1
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

        if not DFS_visit(0):
            return False

        if self.visited != n:
            return False

        return True