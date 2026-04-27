# drug_routing
use neural model to guide a* search of biomedial knowledge graph to find interpretable reasoning paths between drugs and diseases

## Planning:
1. System Arch
    - Knowledge Graph
        - Nodes: drug, gene, protein, diseases
        - Edges: interactions, associations
        - Resources 
            <!-- - DrugBank 
            - STRING database
            - DisGeNET -->
            - API calls (UniProt, Open Targets, MyGene.info, STRING REST API)
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


## Sample Run:
```
INFO __main__: Searching path: DB00945 -> EFO_0000616
INFO kg.api_client: [API] local map: DB00945 -> CHEMBL25
INFO kg.api_client: [API] DB00945 -> 2 targets
INFO kg.graph: [KG] expand(DB00945) type=drug edges=2
INFO kg.api_client: [API] ENSG00000073756 (PTGS2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000073756) type=protein edges=20
INFO kg.api_client: [API] ENSG00000095303 (PTGS1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000095303) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0000685 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000685) type=disease edges=20
INFO kg.graph: [KG] expand(MP_0001914) type=other edges=0
INFO kg.api_client: [API] disease MONDO_0005277 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0005277) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0004274 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0004274) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0000729 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000729) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0005178 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0005178) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0000712 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000712) type=disease edges=20
INFO kg.api_client: [API] disease HP_0002315 -> 20 genes
INFO kg.graph: [KG] expand(HP_0002315) type=disease edges=20
INFO kg.api_client: [API] disease HP_0100607 -> 12 genes
INFO kg.graph: [KG] expand(HP_0100607) type=disease edges=12
INFO kg.api_client: [API] disease EFO_0003898 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0003898) type=disease edges=20
INFO kg.api_client: [API] disease HP_0012531 -> 20 genes
INFO kg.graph: [KG] expand(HP_0012531) type=disease edges=20
INFO kg.api_client: [API] disease HP_0001945 -> 20 genes
INFO kg.graph: [KG] expand(HP_0001945) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0002609 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0002609) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0002258 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0002258) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0005856 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0005856) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0007214 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0007214) type=disease edges=20
INFO kg.api_client: [API] disease HP_0001742 -> 20 genes
INFO kg.graph: [KG] expand(HP_0001742) type=disease edges=20
INFO kg.api_client: [API] disease HP_0001643 -> 20 genes
INFO kg.graph: [KG] expand(HP_0001643) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0005755 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0005755) type=disease edges=20
INFO kg.api_client: [API] disease HP_0012735 -> 20 genes
INFO kg.graph: [KG] expand(HP_0012735) type=disease edges=20
INFO kg.graph: [KG] expand(MP_0001845) type=other edges=0
INFO kg.api_client: [API] disease EFO_0010072 -> 12 genes
INFO kg.graph: [KG] expand(EFO_0010072) type=disease edges=12
INFO kg.api_client: [API] ENSG00000144285 (SCN1A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000144285) type=protein edges=20
INFO kg.api_client: [API] ENSG00000018625 (ATP1A2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000018625) type=protein edges=20
INFO kg.api_client: [API] ENSG00000213689 (TREX1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000213689) type=protein edges=20
INFO kg.api_client: [API] ENSG00000103313 (MEFV) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000103313) type=protein edges=20
INFO kg.api_client: [API] ENSG00000141837 (CACNA1A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000141837) type=protein edges=20
INFO kg.api_client: [API] ENSG00000115267 (IFIH1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000115267) type=protein edges=20
INFO kg.api_client: [API] ENSG00000160710 (ADAR) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000160710) type=protein edges=20
INFO kg.api_client: [API] ENSG00000110921 (MVK) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000110921) type=protein edges=20
INFO kg.api_client: [API] ENSG00000162711 (NLRP3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000162711) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0100135 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0100135) type=disease edges=20
INFO kg.api_client: [API] ENSG00000138829 (FBN2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000138829) type=protein edges=20
INFO kg.api_client: [API] ENSG00000167207 (NOD2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000167207) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0011461 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0011461) type=disease edges=2
INFO kg.api_client: [API] ENSG00000067182 (TNFRSF1A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000067182) type=protein edges=20
INFO kg.api_client: [API] ENSG00000101347 (SAMHD1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000101347) type=protein edges=20
INFO kg.graph: [KG] expand(Orphanet_36387) type=other edges=0
INFO kg.api_client: [API] ENSG00000196664 (TLR7) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000196664) type=protein edges=20
INFO kg.api_client: [API] ENSG00000134250 (NOTCH2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000134250) type=protein edges=20
INFO kg.api_client: [API] ENSG00000102575 (ACP5) -> 12 diseases
INFO kg.graph: [KG] expand(ENSG00000102575) type=protein edges=12
INFO kg.api_client: [API] ENSG00000093072 (ADA2) -> 13 diseases
INFO kg.graph: [KG] expand(ENSG00000093072) type=protein edges=13
INFO kg.api_client: [API] ENSG00000197891 (SLC22A12) -> 13 diseases
INFO kg.graph: [KG] expand(ENSG00000197891) type=protein edges=13
INFO kg.api_client: [API] ENSG00000118503 (TNFAIP3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000118503) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0009849 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0009849) type=disease edges=3
INFO kg.api_client: [API] disease MONDO_0011232 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0011232) type=disease edges=1
INFO kg.api_client: [API] ENSG00000104889 (RNASEH2A) -> 7 diseases
INFO kg.graph: [KG] expand(ENSG00000104889) type=protein edges=7
INFO kg.api_client: [API] disease MONDO_0007363 -> 7 genes
INFO kg.graph: [KG] expand(MONDO_0007363) type=disease edges=7
INFO kg.api_client: [API] ENSG00000136695 (IL36RN) -> 8 diseases
INFO kg.graph: [KG] expand(ENSG00000136695) type=protein edges=8
INFO kg.api_client: [API] ENSG00000136104 (RNASEH2B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000136104) type=protein edges=20
INFO kg.api_client: [API] ENSG00000172922 (RNASEH2C) -> 14 diseases
INFO kg.graph: [KG] expand(ENSG00000172922) type=protein edges=14
INFO kg.api_client: [API] disease MONDO_0014007 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0014007) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0009165 -> 4 genes
INFO kg.graph: [KG] expand(MONDO_0009165) type=disease edges=4
INFO kg.api_client: [API] disease MONDO_0012481 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0012481) type=disease edges=2
INFO kg.api_client: [API] disease EFO_0000474 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000474) type=disease edges=20
INFO kg.api_client: [API] ENSG00000154124 (OTULIN) -> 15 diseases
INFO kg.graph: [KG] expand(ENSG00000154124) type=protein edges=15
INFO kg.api_client: [API] disease MONDO_0011776 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0011776) type=disease edges=20
INFO kg.graph: [KG] expand(Orphanet_97) type=other edges=0
INFO kg.api_client: [API] disease MONDO_0007163 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0007163) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0008523 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0008523) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0007483 -> 4 genes
INFO kg.graph: [KG] expand(MONDO_0007483) type=disease edges=4
INFO kg.api_client: [API] disease MONDO_0020756 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0020756) type=disease edges=2
INFO kg.api_client: [API] disease MONDO_0014367 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0014367) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0012320 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0012320) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0014917 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0014917) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0018088 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0018088) type=disease edges=20
INFO kg.api_client: [API] ENSG00000105397 (TYK2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000105397) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0009572 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0009572) type=disease edges=1
INFO kg.api_client: [API] ENSG00000154122 (ANKH) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000154122) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0007727 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0007727) type=disease edges=2
INFO kg.api_client: [API] disease MONDO_0008641 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0008641) type=disease edges=2
INFO kg.api_client: [API] ENSG00000180210 (F2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000180210) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0008633 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0008633) type=disease edges=3
INFO kg.api_client: [API] disease MONDO_0011959 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0011959) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_32960) type=other edges=0
INFO kg.api_client: [API] disease MONDO_0007349 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0007349) type=disease edges=1
INFO kg.api_client: [API] ENSG00000113302 (IL12B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000113302) type=protein edges=20
INFO kg.api_client: [API] ENSG00000160712 (IL6R) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000160712) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0100062 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0100062) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0008457 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0008457) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0007915 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0007915) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0009960 -> 6 genes
INFO kg.graph: [KG] expand(MONDO_0009960) type=disease edges=6
INFO kg.api_client: [API] disease MONDO_0007087 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0007087) type=disease edges=3
INFO kg.api_client: [API] disease MONDO_0024535 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0024535) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0014306 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0014306) type=disease edges=1
INFO kg.api_client: [API] ENSG00000110680 (CALCA) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000110680) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0007057 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0007057) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_51) type=other edges=0
INFO kg.api_client: [API] disease MONDO_0011939 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0011939) type=disease edges=2
INFO kg.api_client: [API] ENSG00000232810 (TNF) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000232810) type=protein edges=20
INFO kg.api_client: [API] ENSG00000158125 (XDH) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000158125) type=protein edges=20
INFO kg.api_client: [API] ENSG00000056972 (TRAF3IP2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000056972) type=protein edges=20
INFO kg.api_client: [API] ENSG00000240972 (MIF) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000240972) type=protein edges=20
INFO kg.api_client: [API] disease HP_0001250 -> 20 genes
INFO kg.graph: [KG] expand(HP_0001250) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0000384 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000384) type=disease edges=20
INFO kg.api_client: [API] ENSG00000118777 (ABCG2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000118777) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0012500 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0012500) type=disease edges=2
INFO kg.api_client: [API] disease MONDO_0013626 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0013626) type=disease edges=3
INFO kg.api_client: [API] ENSG00000096968 (JAK2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000096968) type=protein edges=20
INFO kg.api_client: [API] ENSG00000162434 (JAK1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000162434) type=protein edges=20
INFO kg.api_client: [API] ENSG00000159339 (PADI4) -> 10 diseases
INFO kg.graph: [KG] expand(ENSG00000159339) type=protein edges=10
INFO kg.api_client: [API] disease MONDO_0008293 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0008293) type=disease edges=3
INFO kg.api_client: [API] disease MONDO_0014912 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0014912) type=disease edges=1
INFO kg.api_client: [API] ENSG00000198734 (F5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000198734) type=protein edges=20
INFO kg.api_client: [API] ENSG00000144481 (TRPM8) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000144481) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0030472 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0030472) type=disease edges=1
INFO kg.api_client: [API] ENSG00000134242 (PTPN22) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000134242) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0012439 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0012439) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0018866 -> 15 genes
INFO kg.graph: [KG] expand(MONDO_0018866) type=disease edges=15
INFO kg.api_client: [API] disease EFO_1001186 -> 1 genes
INFO kg.graph: [KG] expand(EFO_1001186) type=disease edges=1
INFO kg.api_client: [API] ENSG00000113161 (HMGCR) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000113161) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0013059 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0013059) type=disease edges=2
INFO kg.api_client: [API] ENSG00000112115 (IL17A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000112115) type=protein edges=20
INFO kg.api_client: [API] ENSG00000172572 (PDE3A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000172572) type=protein edges=20
INFO kg.api_client: [API] ENSG00000175868 (CALCB) -> 9 diseases
INFO kg.graph: [KG] expand(ENSG00000175868) type=protein edges=9
INFO kg.api_client: [API] disease MONDO_0013361 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0013361) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0800329 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0800329) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0800045 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0800045) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0859204 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0859204) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_3421) type=other edges=0
INFO kg.graph: [KG] expand(Orphanet_63261) type=other edges=0
INFO kg.api_client: [API] ENSG00000168065 (SLC22A11) -> 7 diseases
INFO kg.graph: [KG] expand(ENSG00000168065) type=protein edges=7
INFO kg.api_client: [API] ENSG00000007314 (SCN4A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000007314) type=protein edges=20
INFO kg.graph: [KG] expand(Orphanet_71291) type=other edges=0
INFO kg.api_client: [API] ENSG00000112038 (OPRM1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000112038) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0012429 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0012429) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0012472 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0012472) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_325) type=other edges=0
INFO kg.api_client: [API] disease MONDO_0007319 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0007319) type=disease edges=2
INFO kg.api_client: [API] ENSG00000114013 (CD86) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000114013) type=protein edges=20
INFO kg.api_client: [API] ENSG00000159640 (ACE) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000159640) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0012471 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0012471) type=disease edges=2
INFO kg.api_client: [API] ENSG00000179630 (LACC1) -> 14 diseases
INFO kg.graph: [KG] expand(ENSG00000179630) type=protein edges=14
INFO kg.api_client: [API] disease MONDO_0030692 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0030692) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0015465 -> 5 genes
INFO kg.graph: [KG] expand(MONDO_0015465) type=disease edges=5
INFO kg.api_client: [API] disease MONDO_0016532 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0016532) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0015019 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0015019) type=disease edges=1
INFO kg.api_client: [API] ENSG00000115594 (IL1R1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000115594) type=protein edges=20
INFO kg.api_client: [API] ENSG00000128604 (IRF5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000128604) type=protein edges=20
INFO kg.api_client: [API] ENSG00000125965 (GDF5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000125965) type=protein edges=20
INFO kg.api_client: [API] ENSG00000136531 (SCN2A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000136531) type=protein edges=20
INFO kg.api_client: [API] ENSG00000196876 (SCN8A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000196876) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0007849 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0007849) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_47045) type=other edges=0
INFO kg.api_client: [API] ENSG00000110944 (IL23A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000110944) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0001365 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0001365) type=disease edges=20
INFO kg.api_client: [API] ENSG00000153253 (SCN3A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000153253) type=protein edges=20
INFO kg.api_client: [API] ENSG00000091831 (ESR1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000091831) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0012682 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0012682) type=disease edges=1
INFO kg.api_client: [API] ENSG00000113580 (NR3C1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000113580) type=protein edges=20
INFO kg.api_client: [API] ENSG00000156738 (MS4A1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000156738) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0009295 -> 1 genes
INFO kg.graph: [KG] expand(EFO_0009295) type=disease edges=1
INFO kg.graph: [KG] expand(Orphanet_247691) type=other edges=0
INFO kg.api_client: [API] ENSG00000196689 (TRPV1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000196689) type=protein edges=20
INFO kg.api_client: [API] ENSG00000132170 (PPARG) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000132170) type=protein edges=20
INFO kg.api_client: [API] ENSG00000183873 (SCN5A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000183873) type=protein edges=20
INFO kg.api_client: [API] ENSG00000160856 (FCRL3) -> 11 diseases
INFO kg.graph: [KG] expand(ENSG00000160856) type=protein edges=11
INFO kg.api_client: [API] ENSG00000239732 (TLR9) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000239732) type=protein edges=20
INFO kg.api_client: [API] ENSG00000166206 (GABRB3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000166206) type=protein edges=20
INFO kg.api_client: [API] ENSG00000022355 (GABRA1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000022355) type=protein edges=20
INFO kg.api_client: [API] ENSG00000113327 (GABRG2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000113327) type=protein edges=20
INFO kg.api_client: [API] ENSG00000102967 (DHODH) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000102967) type=protein edges=20
INFO kg.api_client: [API] ENSG00000121594 (CD80) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000121594) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0016241 -> 15 genes
INFO kg.graph: [KG] expand(MONDO_0016241) type=disease edges=15
INFO kg.api_client: [API] ENSG00000117394 (SLC2A1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000117394) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0019587 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0019587) type=disease edges=20
INFO kg.api_client: [API] ENSG00000183454 (GRIN2A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000183454) type=protein edges=20
INFO kg.api_client: [API] ENSG00000135312 (HTR1B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000135312) type=protein edges=20
INFO kg.api_client: [API] ENSG00000094755 (GABRP) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000094755) type=protein edges=20
INFO kg.api_client: [API] ENSG00000145864 (GABRB2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000145864) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0000700 -> 4 genes
INFO kg.graph: [KG] expand(MONDO_0000700) type=disease edges=4
INFO kg.api_client: [API] disease EFO_0002429 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0002429) type=disease edges=20
INFO kg.api_client: [API] ENSG00000117480 (FAAH) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000117480) type=protein edges=20
INFO kg.api_client: [API] ENSG00000109667 (SLC2A9) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000109667) type=protein edges=20
INFO kg.api_client: [API] ENSG00000155511 (GRIA1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000155511) type=protein edges=20
INFO kg.api_client: [API] ENSG00000134259 (NGF) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000134259) type=protein edges=20
INFO kg.api_client: [API] ENSG00000107147 (KCNT1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000107147) type=protein edges=20
INFO kg.api_client: [API] ENSG00000102287 (GABRE) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000102287) type=protein edges=20
INFO kg.api_client: [API] ENSG00000268089 (GABRQ) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000268089) type=protein edges=20
INFO kg.api_client: [API] ENSG00000136854 (STXBP1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000136854) type=protein edges=20
INFO kg.api_client: [API] ENSG00000128271 (ADORA2A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000128271) type=protein edges=20
INFO kg.api_client: [API] ENSG00000179546 (HTR1D) -> 19 diseases
INFO kg.graph: [KG] expand(ENSG00000179546) type=protein edges=19
INFO kg.api_client: [API] disease MONDO_0008559 -> 6 genes
INFO kg.graph: [KG] expand(MONDO_0008559) type=disease edges=6
INFO kg.api_client: [API] ENSG00000008086 (CDKL5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000008086) type=protein edges=20
INFO kg.api_client: [API] ENSG00000165194 (PCDH19) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000165194) type=protein edges=20
INFO kg.api_client: [API] ENSG00000011677 (GABRA3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000011677) type=protein edges=20
INFO kg.api_client: [API] ENSG00000109158 (GABRA4) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000109158) type=protein edges=20
INFO kg.api_client: [API] ENSG00000100150 (DEPDC5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000100150) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0008560 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0008560) type=disease edges=1
INFO kg.api_client: [API] ENSG00000160213 (CSTB) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000160213) type=protein edges=20
INFO kg.api_client: [API] ENSG00000012779 (ALOX5) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000012779) type=protein edges=20
INFO kg.api_client: [API] ENSG00000075043 (KCNQ2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000075043) type=protein edges=20
INFO kg.api_client: [API] ENSG00000186153 (WWOX) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000186153) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0009104 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0009104) type=disease edges=20
INFO kg.api_client: [API] ENSG00000153956 (CACNA2D1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000153956) type=protein edges=20
INFO kg.api_client: [API] ENSG00000139626 (ITGB7) -> 9 diseases
INFO kg.graph: [KG] expand(ENSG00000139626) type=protein edges=9
INFO kg.api_client: [API] disease MONDO_0010209 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0010209) type=disease edges=2
INFO kg.api_client: [API] ENSG00000169313 (P2RY12) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000169313) type=protein edges=20
INFO kg.api_client: [API] ENSG00000187566 (NHLRC1) -> 7 diseases
INFO kg.graph: [KG] expand(ENSG00000187566) type=protein edges=7
INFO kg.api_client: [API] ENSG00000115232 (ITGA4) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000115232) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0007318 -> 5 genes
INFO kg.graph: [KG] expand(MONDO_0007318) type=disease edges=5
INFO kg.api_client: [API] disease EFO_0003778 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0003778) type=disease edges=20
INFO kg.api_client: [API] ENSG00000126218 (F10) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000126218) type=protein edges=20
INFO kg.api_client: [API] ENSG00000164116 (GUCY1A1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000164116) type=protein edges=20
INFO kg.api_client: [API] ENSG00000105639 (JAK3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000105639) type=protein edges=20
INFO kg.api_client: [API] ENSG00000123416 (TUBA1B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000123416) type=protein edges=20
INFO kg.api_client: [API] ENSG00000196230 (TUBB) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000196230) type=protein edges=20
INFO kg.api_client: [API] ENSG00000101162 (TUBB1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000101162) type=protein edges=20
INFO kg.api_client: [API] ENSG00000104833 (TUBB4A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000104833) type=protein edges=20
INFO kg.api_client: [API] ENSG00000137267 (TUBB2A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000137267) type=protein edges=20
INFO kg.api_client: [API] ENSG00000137285 (TUBB2B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000137285) type=protein edges=20
INFO kg.api_client: [API] ENSG00000167552 (TUBA1A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000167552) type=protein edges=20
INFO kg.api_client: [API] ENSG00000167553 (TUBA1C) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000167553) type=protein edges=20
INFO kg.api_client: [API] ENSG00000176014 (TUBB6) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000176014) type=protein edges=20
INFO kg.api_client: [API] ENSG00000188229 (TUBB4B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000188229) type=protein edges=20
INFO kg.api_client: [API] ENSG00000198033 (TUBA3C) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000198033) type=protein edges=20
INFO kg.api_client: [API] ENSG00000258947 (TUBB3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000258947) type=protein edges=20
INFO kg.api_client: [API] ENSG00000261456 (TUBB8) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000261456) type=protein edges=20
INFO kg.api_client: [API] ENSG00000147955 (SIGMAR1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000147955) type=protein edges=20
INFO kg.api_client: [API] ENSG00000136634 (IL10) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000136634) type=protein edges=20
INFO kg.api_client: [API] ENSG00000171873 (ADRA1D) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000171873) type=protein edges=20
INFO kg.api_client: [API] ENSG00000169432 (SCN9A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000169432) type=protein edges=20
INFO kg.api_client: [API] ENSG00000185313 (SCN10A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000185313) type=protein edges=20
INFO kg.api_client: [API] ENSG00000168356 (SCN11A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000168356) type=protein edges=20
INFO kg.api_client: [API] ENSG00000116329 (OPRD1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000116329) type=protein edges=20
INFO kg.api_client: [API] ENSG00000120907 (ADRA1A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000120907) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0009210 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0009210) type=disease edges=2
INFO kg.api_client: [API] ENSG00000157445 (CACNA2D3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000157445) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0002009 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0002009) type=disease edges=20
INFO kg.api_client: [API] ENSG00000144891 (AGTR1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000144891) type=protein edges=20
INFO kg.api_client: [API] ENSG00000170214 (ADRA1B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000170214) type=protein edges=20
INFO kg.api_client: [API] ENSG00000081248 (CACNA1S) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000081248) type=protein edges=20
INFO kg.api_client: [API] ENSG00000104368 (PLAT) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000104368) type=protein edges=20
INFO kg.api_client: [API] ENSG00000082556 (OPRK1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000082556) type=protein edges=20
INFO kg.api_client: [API] ENSG00000162594 (IL23R) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000162594) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0031030 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0031030) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0020586 -> 3 genes
INFO kg.graph: [KG] expand(MONDO_0020586) type=disease edges=3
INFO kg.api_client: [API] ENSG00000196639 (HRH1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000196639) type=protein edges=20
INFO kg.api_client: [API] ENSG00000152952 (PLOD2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000152952) type=protein edges=20
INFO kg.api_client: [API] ENSG00000170989 (S1PR1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000170989) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0019557 -> 5 genes
INFO kg.graph: [KG] expand(MONDO_0019557) type=disease edges=5
INFO kg.api_client: [API] ENSG00000168811 (IL12A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000168811) type=protein edges=20
INFO kg.api_client: [API] ENSG00000050628 (PTGER3) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000050628) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0002430 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0002430) type=disease edges=20
INFO kg.api_client: [API] disease HP_0000924 -> 20 genes
INFO kg.graph: [KG] expand(HP_0000924) type=disease edges=20
INFO kg.api_client: [API] ENSG00000103546 (SLC6A2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000103546) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0009903 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0009903) type=disease edges=1
INFO kg.api_client: [API] ENSG00000043591 (ADRB1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000043591) type=protein edges=20
INFO kg.api_client: [API] ENSG00000104321 (TRPA1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000104321) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0009071 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0009071) type=disease edges=2
INFO kg.api_client: [API] ENSG00000150594 (ADRA2A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000150594) type=protein edges=20
INFO kg.api_client: [API] ENSG00000184160 (ADRA2C) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000184160) type=protein edges=20
INFO kg.api_client: [API] ENSG00000274286 (ADRA2B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000274286) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0000373 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000373) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0031384 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0031384) type=disease edges=2
INFO kg.api_client: [API] ENSG00000187498 (COL4A1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000187498) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0003907 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0003907) type=disease edges=20
INFO kg.api_client: [API] ENSG00000169252 (ADRB2) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000169252) type=protein edges=20
INFO kg.api_client: [API] disease HP_0000989 -> 20 genes
INFO kg.graph: [KG] expand(HP_0000989) type=disease edges=20
INFO kg.api_client: [API] ENSG00000180739 (S1PR5) -> 10 diseases
INFO kg.graph: [KG] expand(ENSG00000180739) type=protein edges=10
INFO kg.api_client: [API] disease MONDO_0011448 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0011448) type=disease edges=2
INFO kg.api_client: [API] ENSG00000151067 (CACNA1C) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000151067) type=protein edges=20
INFO kg.api_client: [API] ENSG00000228716 (DHFR) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000228716) type=protein edges=20
INFO kg.api_client: [API] disease EFO_0004251 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0004251) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0009552 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0009552) type=disease edges=20
INFO kg.api_client: [API] ENSG00000184588 (PDE4B) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000184588) type=protein edges=20
INFO kg.api_client: [API] disease HP_0003124 -> 20 genes
INFO kg.graph: [KG] expand(HP_0003124) type=disease edges=20
INFO kg.graph: [KG] expand(Orphanet_1276) type=other edges=0
INFO kg.api_client: [API] ENSG00000102001 (CACNA1F) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000102001) type=protein edges=20
INFO kg.api_client: [API] ENSG00000157388 (CACNA1D) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000157388) type=protein edges=20
INFO kg.api_client: [API] ENSG00000128059 (PPAT) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000128059) type=protein edges=20
INFO kg.api_client: [API] ENSG00000060718 (COL11A1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000060718) type=protein edges=20
INFO kg.api_client: [API] ENSG00000082175 (PGR) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000082175) type=protein edges=20
INFO kg.api_client: [API] ENSG00000136546 (SCN7A) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000136546) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0021187 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0021187) type=disease edges=20
INFO kg.api_client: [API] ENSG00000171560 (FGA) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000171560) type=protein edges=20
INFO kg.api_client: [API] ENSG00000125910 (S1PR4) -> 13 diseases
INFO kg.graph: [KG] expand(ENSG00000125910) type=protein edges=13
INFO kg.api_client: [API] disease MONDO_0100096 -> 20 genes
INFO kg.graph: [KG] expand(MONDO_0100096) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0000401 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0000401) type=disease edges=20
INFO kg.api_client: [API] disease MONDO_0002247 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0002247) type=disease edges=1
INFO kg.api_client: [API] disease EFO_0004270 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0004270) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0003144 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0003144) type=disease edges=20
INFO kg.api_client: [API] disease EFO_0001645 -> 20 genes
INFO kg.graph: [KG] expand(EFO_0001645) type=disease edges=20
INFO kg.api_client: [API] ENSG00000087258 (GNAO1) -> 20 diseases
INFO kg.graph: [KG] expand(ENSG00000087258) type=protein edges=20
INFO kg.api_client: [API] disease MONDO_0024307 -> 1 genes
INFO kg.graph: [KG] expand(MONDO_0024307) type=disease edges=1
INFO kg.api_client: [API] disease MONDO_0007221 -> 2 genes
INFO kg.graph: [KG] expand(MONDO_0007221) type=disease edges=2

=== Path found ===
[drug] DB00945
  → [protein] ENSG00000095303
    → [disease] HP_0100607
      → [protein] ENSG00000082175
        → [disease] EFO_0000616

Total cost: 1.2822  (=4 hops)
```