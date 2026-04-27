import logging
from kg.api_client import APIClient
from kg.graph import KnowledgeGraph
from search.astar import AStarSearch

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)


def main():
    api = APIClient()
    kg = KnowledgeGraph(api)
    search = AStarSearch(kg)

    # DB00945 = Aspirin
    # EFO_0000616 = Cancer (broad EFO term accepted by Open Targets)
    # Try EFO_0000249 (Alzheimer's) or EFO_0003767 (colorectal cancer) for tighter paths
    start = "DB00945"
    goal = "EFO_0000616"

    log.info("Searching path: %s -> %s", start, goal)
    path, cost = search.search(start, goal, max_depth=6)

    if path:
        print("\n=== Path found ===")
        for i, node in enumerate(path):
            t = kg.node_type(node)
            prefix = "  " * i + "→ " if i else ""
            print(f"{prefix}[{t}] {node}")
        print(f"\nTotal cost: {cost:.4f}  (={len(path)-1} hops)")
    else:
        print("\nNo path found within max_depth.")
        print(f"Nodes visited: {len(kg.expanded)}")
        print(f"Edges in graph: {kg.g.number_of_edges()}")


if __name__ == "__main__":
    main()