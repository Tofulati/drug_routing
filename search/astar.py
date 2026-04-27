import heapq
import logging
import math

log = logging.getLogger(__name__)
_HOP_ESTIMATES = {
    ("drug", "disease"): 2,
    ("drug", "protein"): 1,
    ("protein", "disease"): 1,
    ("protein", "protein"): 1,
    ("disease", "disease"): 0,
}
HOP_COST = 0.1


class AStarSearch:
    def __init__(self, kg):
        self.kg = kg

    def edge_cost(self, u: str, v: str) -> float:
        if not self.kg.g.has_edge(u, v):
            return 1.0
        w = self.kg.g[u][v].get("weight", 1.0)
        return -math.log(max(w, 1e-6))

    def heuristic(self, node: str, goal: str) -> float:
        """Admissible type-transition heuristic.
        Returns a lower bound on remaining cost based on how many
        type hops are still needed to reach the goal's type."""
        if node == goal:
            return 0.0
        nt = self.kg.node_type(node)
        gt = self.kg.node_type(goal)
        hops = _HOP_ESTIMATES.get((nt, gt), 0)
        return hops * HOP_COST

    def search(
        self, start: str, goal: str, max_depth: int = 6
    ) -> tuple[list[str] | None, float]:
        self.kg.g.add_node(start)
        self.kg.g.add_node(goal)

        came_from: dict[str, str | None] = {start: None}
        best_cost: dict[str, float] = {}

        pq: list[tuple[float, float, str]] = []
        h0 = self.heuristic(start, goal)
        heapq.heappush(pq, (h0, 0.0, start))

        while pq:
            f, g, node = heapq.heappop(pq)

            if node == goal:
                return self._reconstruct(came_from, goal), g

            if node in best_cost and best_cost[node] <= g:
                continue
            best_cost[node] = g

            if len(self._reconstruct(came_from, node)) > max_depth:
                continue

            log.debug("[VISIT] %s  g=%.4f  f=%.4f", node, g, f)

            for nb in self.kg.neighbors(node):
                new_g = g + self.edge_cost(node, nb)
                if nb in best_cost and best_cost[nb] <= new_g:
                    continue
                came_from[nb] = node
                priority = new_g + self.heuristic(nb, goal)
                heapq.heappush(pq, (priority, new_g, nb))

        return None, float("inf")

    def _reconstruct(self, came_from: dict, node: str) -> list[str]:
        path = []
        cur = node
        while cur is not None:
            path.append(cur)
            cur = came_from.get(cur)
        return list(reversed(path))