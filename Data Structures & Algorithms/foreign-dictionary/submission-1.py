from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set()
        for word in words:
            for char in word:
                chars.add(char)

        # Create graph
        self.adjacency_list = {char : set() for char in chars}
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]                
                l1, l2 = 0, 0
                while l1 < len(w1) and l2 < len(w2):
                    chars.add(w1[l1])
                    chars.add(w2[l2])
                    if w1[l1] == w2[l2]:
                        l1 += 1
                        l2 += 1
                    else:
                        break
                    
                if l1 == len(w1) or l2 == len(w2):
                    if len(w1) > len(w2):
                        return ""
                    continue

                self.adjacency_list[w2[l2]].add(w1[l1])

        print(self.adjacency_list)   
        print(chars)                 

        # Kahn's Topo Sort:
        indeg = {i : 0 for i in chars}
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                indeg[v] += 1

        # print(indeg)

        q = deque(i for i in list(self.adjacency_list.keys()) if indeg[i] == 0)
        # print(q)
        return_string = ""

        while q:
            u = q.popleft()
            return_string += str(u)
            for v in self.adjacency_list[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        print(indeg)

        return return_string[::-1] if len(return_string) == len(chars) else ""

