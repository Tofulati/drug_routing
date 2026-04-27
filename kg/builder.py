from kg.graph import KnowledgeGraph

def build_toy_kg():
    kg = KnowledgeGraph()

    kg.add_node("DrugA", "drug")
    kg.add_node("Protein1", "protein")
    kg.add_node("Protein2", "protein")
    kg.add_node("GeneX", "gene")
    kg.add_node("DiseaseZ", "disease")

    kg.add_edge("DrugA", "Protein1", "targets", 0.9)
    kg.add_edge("Protein1", "Protein2", "interacts", 0.8)
    kg.add_edge("Protein2", "GeneX", "regulates", 0.85)
    kg.add_edge("GeneX", "DiseaseZ", "associated", 0.95)

    return kg