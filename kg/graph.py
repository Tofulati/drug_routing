import logging
import networkx as nx

log = logging.getLogger(__name__)
MAX_FANOUT = 25

class KnowledgeGraph:
    def __init__(self, api):
        self.g = nx.DiGraph()
        self.api = api
        self.expanded = set()

    def add_edge(self, u, v, t, w):
        self.g.add_node(u)
        self.g.add_node(v)
        self.g.add_edge(u, v, type=t, weight=w)

    def node_type(self, node: str) -> str:
        if node.startswith(("DB", "CHEMBL")):
            return "drug"
        if node.startswith(("ENSG", "P", "Q")):
            return "protein"
        if node.startswith(("EFO", "MONDO", "HP", "OMIM", "C")):
            return "disease"
        return "other"

    def neighbors(self, node: str) -> list[str]:
        if node not in self.g:
            self.g.add_node(node)
        if node not in self.expanded:
            self.expand(node)
        return list(self.g.successors(node))

    def expand(self, node: str):
        if node in self.expanded:
            return
        self.expanded.add(node)

        t = self.node_type(node)
        edges = []
        if t == "drug":
            edges = self.api.get_drug_targets(node)
        elif t == "protein":
            edges = self.api.get_protein_neighbors(node)
        elif t == "disease":
            edges = self.api.get_gene_disease(node)
        else:
            log.debug("[KG] Skipping expansion of unknown node type: %s", node)

        edges = edges[:MAX_FANOUT]
        log.info("[KG] expand(%s) type=%s edges=%d", node, t, len(edges))

        for u, v, r, w in edges:
            self.add_edge(u, v, r, w)