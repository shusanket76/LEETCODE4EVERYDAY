class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set(x for x in range(n))
        for x in edges:
            if x[1] in visited:
                visited.remove(x[1])
        return list(visited)

        