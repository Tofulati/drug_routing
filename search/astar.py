import heapq
import math

class AStarSearch:
    def __init__(self, kg):
        self.kg = kg

    def edge_cost(self, u, v):
        weight = self.kg.edge_data(u, v).get("weight", 1.0)
        return -math.log(weight + 1e-9)
    
    def heuristic(self, node, goal):
        return 0.0

    def search(self, start, goal, max_depth = 6):
        pq = []
        heapq.heappush(pq, (0, start, [start]))

        best = {}

        while pq:
            cost, node, path = heapq.heappop(pq)

            if node == goal:
                return path, cost
        
            if len(path) > max_depth:
                continue
                
            if (node in best) and (best[node] <= cost):
                continue

            best[node] = cost

            for neighbor in self.kg.neighbors(node):
                new_cost = cost + self.edge_cost(node, neighbor)
                priority = new_cost + self.heuristic(neighbor, goal)

                heapq.heappush(pq, (priority, neighbor, path + [neighbor]))

        return None, float('inf')