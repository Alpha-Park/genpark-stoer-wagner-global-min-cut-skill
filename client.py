class StoerWagnerMinCut:
    """Stoer-Wagner global minimum cut solver."""
    def find_min_cut(self, n: int, adj_matrix: list[list[float]]) -> dict:
        mat = [row[:] for row in adj_matrix]
        vertices = list(range(n))
        min_cut = float('inf')

        for phase in range(n - 1):
            w = [0.0] * len(vertices)
            added = [False] * len(vertices)
            prev, last = None, None

            for _ in range(len(vertices)):
                best_v = -1
                best_w = -1.0
                for i in range(len(vertices)):
                    if not added[i] and w[i] > best_w:
                        best_w = w[i]
                        best_v = i

                added[best_v] = True
                prev = last
                last = best_v

                for i in range(len(vertices)):
                    if not added[i]:
                        w[i] += mat[vertices[best_v]][vertices[i]]

            if best_w < min_cut:
                min_cut = best_w

            # Merge prev and last
            u, v = vertices[prev], vertices[last]
            for i in range(n):
                mat[u][i] += mat[v][i]
                mat[i][u] = mat[u][i]
            vertices.pop(last)

        return {
            "num_vertices": n,
            "global_min_cut_weight": min_cut
        }
