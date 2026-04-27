import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, node_type):
        self.graph.add_node(node_id, type=node_type)

    def add_edge(self, u, v, edge_type, weight = 1.0):
        self.graph.add_edge(u, v, type=edge_type, weight=weight)
    
    def neighbors(self, node):
        return list(self.graph.successors(node))

    def node_type(self, node):
        return self.graph.nodes[node]["type"]

    def edge_data(self, u, v):
        return self.graph.edges[u, v]