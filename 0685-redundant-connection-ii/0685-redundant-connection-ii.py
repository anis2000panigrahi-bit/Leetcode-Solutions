class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)

        parent = [0] * (n + 1)

        candidate1 = None
        candidate2 = None

        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(n + 1))

        for u, v in edges:
            if candidate2 and [u, v] == candidate2:
                continue

            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                if candidate1:
                    return candidate1
                return [u, v]

            parent[root_v] = root_u

        return candidate2