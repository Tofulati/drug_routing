# drug_routing
use neural model to guide a* search of biomedial knowledge graph to find interpretable reasoning paths between drugs and diseases

## Planning:
1. System Arch
    - Knowledge Graph
        - Nodes: drug, gene, protein, diseases
        - Edges: interactions, associations
        - Resources
            - DrugBank
            - STRING database
            - DisGeNET
        - Drug -> Protein -> Gene -> Disease
    - Scores
        - f(u, v, type) -> score
        - GNN?
        - output: probs edge for reasoning
    - A* Search
        - given g(n) + h(n) -> path
2. Search Problem
    - State: current nodes
    - Start: drug node, Goal: disease node
    - Heuristic:
        - Shortest distance (computed easily)
        - Similarity between current and disease
        - Train model on node and prob to disease
3. Bio Constraints
    - Must traverse path, not jump (adjacency)
    - Path length constraints? (long = bad?)
    - Rules?
        - drug -> target -> protein
        - protein -> interact -> gene/protein?
        - gene/protein -> associate -> disease?
    - Constrained A*
    - Curated: Reactome (restrict to nodes in same pathway neighborhood)
4. Algo
    - Train edges score
    - Run A*
    - Return top-k path
5. Eval
    - Pred Acc:
        - predict drug-disease link
        - Hits@K, MRR
    - Path QA:
        - interpretable
        - biological relevance (genes are involved)
        - compare baseline (random, shortest path, GNN)
    - Case study:
        - choose disease, show path and bio explaination
