from kg.builder import build_toy_kg
from search.astar import AStarSearch

def main():
    kg = build_toy_kg()

    searcher = AStarSearch(kg)

    path, cost = searcher.search("DrugA", "DiseaseZ")

    print("Path:", path)
    print("Cost:", cost)

if __name__ == "__main__":
    main()