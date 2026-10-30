class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        pq = [(0, 0, 1)]
        dist = {}
        while pq:
            cost, node, count = heapq.heappop(pq)
            if node == n - 1:
                return cost
            if (node, count) in dist:
                continue
            dist[(node, count)] = cost
            for nei, w in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1
                if new_count <= k and (nei, new_count) not in dist:
                    heapq.heappush(
                        pq,
                        (cost + w, nei, new_count)
                    )

        return -1