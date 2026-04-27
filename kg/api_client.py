import requests
import logging

log = logging.getLogger(__name__)
OT_URL = "https://api.platform.opentargets.org/api/v4/graphql"


class APIClient:
    def get_drug_targets(self, drug_id: str) -> list[tuple]:
        chembl_id = self.drugbank_to_chembl(drug_id)
        if not chembl_id:
            log.warning("[API] No ChEMBL ID for %s, skipping", drug_id)
            return []

        query = {
            "query": """
            query ($id: String!) {
              drug(chemblId: $id) {
                mechanismsOfAction {
                  rows {
                    targets { id approvedSymbol }
                    actionType
                  }
                }
              }
            }
            """,
            "variables": {"id": chembl_id},
        }
        try:
            r = requests.post(OT_URL, json=query, timeout=10)
            r.raise_for_status()
            
            data = r.json().get("data") or {}
            drug = data.get("drug") or {}
            moa = drug.get("mechanismsOfAction") or {}
            rows = moa.get("rows") or []

            edges = [
                (drug_id, t["id"], "targets", 0.9)
                for row in rows
                for t in row.get("targets", [])
            ]
            
            log.info("[API] %s -> %d targets", drug_id, len(edges))
            return edges
            
        except Exception as e:
            log.warning("[API] get_drug_targets failed for %s: %s", drug_id, e)
            return []

    def get_protein_neighbors(self, ensembl_id: str) -> list[tuple]:
        query = {
            "query": """
            query ($id: String!) {
              target(ensemblId: $id) {
                approvedSymbol
                associatedDiseases(page: {index: 0, size: 20}) {
                  rows {
                    disease { id name }
                    score
                  }
                }
              }
            }
            """,
            "variables": {"id": ensembl_id},
        }
        try:
            r = requests.post(OT_URL, json=query, timeout=10)
            r.raise_for_status()
            data = r.json().get("data", {}).get("target")
            if not data:
                log.warning("[API] No target data for %s", ensembl_id)
                return []
            symbol = data.get("approvedSymbol", ensembl_id)
            rows = data.get("associatedDiseases", {}).get("rows", [])
            edges = [
                (ensembl_id, row["disease"]["id"], "associated", float(row["score"]))
                for row in rows
                if row.get("disease") and row.get("score", 0) > 0.1
            ]
            log.info("[API] %s (%s) -> %d diseases", ensembl_id, symbol, len(edges))
            return edges
        except Exception as e:
            log.warning("[API] get_protein_neighbors failed for %s: %s", ensembl_id, e)
            return []

    def get_gene_disease(self, disease_id: str) -> list[tuple]:
        query = {
            "query": """
            query ($id: String!) {
              disease(efoId: $id) {
                name
                associatedTargets(page: {index: 0, size: 20}) {
                  rows {
                    target { id approvedSymbol }
                    score
                  }
                }
              }
            }
            """,
            "variables": {"id": disease_id},
        }
        try:
            r = requests.post(OT_URL, json=query, timeout=10)
            r.raise_for_status()
            data = r.json().get("data", {}).get("disease")
            if not data:
                log.warning("[API] No disease data for %s", disease_id)
                return []
            rows = data.get("associatedTargets", {}).get("rows", [])
            
            # FIX: Swap target_id and disease_id so the edge flows outward
            edges = [
                (disease_id, row["target"]["id"], "associated", float(row["score"]))
                for row in rows
                if row.get("target") and row.get("score", 0) > 0.1
            ]
            
            log.info("[API] disease %s -> %d genes", disease_id, len(edges))
            return edges
        except Exception as e:
            log.warning("[API] get_gene_disease failed for %s: %s", disease_id, e)
            return []

    _DB_TO_CHEMBL: dict[str, str] = {
        "DB00945": "CHEMBL25",
        "DB00316": "CHEMBL185",
        "DB00331": "CHEMBL714",
        "DB01050": "CHEMBL521",
        "DB00563": "CHEMBL34259",
        "DB00530": "CHEMBL553",
    }

    def drugbank_to_chembl(self, drugbank_id: str) -> str | None:
        if drugbank_id in self._DB_TO_CHEMBL:
            chembl = self._DB_TO_CHEMBL[drugbank_id]
            log.info("[API] local map: %s -> %s", drugbank_id, chembl)
            return chembl

        try:
            url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"
            payload = {"type": "sourceID", "compound": drugbank_id, "sourceID": 22}
            r = requests.post(url, json=payload, timeout=10)
            r.raise_for_status()
            body = r.json()
            compounds = body.get("compounds", body) if isinstance(body, dict) else body
            for compound in compounds:
                for source in compound.get("sources", []):
                    if source.get("sourceID") == 1 or source.get("shortName", "").lower() == "chembl":
                        chembl = source.get("compoundId") or source.get("src_compound_id")
                        if chembl:
                            log.info("[API] UniChem: %s -> %s", drugbank_id, chembl)
                            return chembl
        except Exception as e:
            log.warning("[API] UniChem failed for %s: %s", drugbank_id, e)

        try:
            url = "https://www.ebi.ac.uk/chembl/api/data/molecule.json"
            params = {"molecule_synonyms__synonyms__iexact": drugbank_id, "limit": 1}
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            mols = r.json().get("molecules", [])
            if mols:
                chembl = mols[0]["molecule_chembl_id"]
                log.info("[API] ChEMBL synonym: %s -> %s", drugbank_id, chembl)
                return chembl
        except Exception as e:
            log.warning("[API] ChEMBL synonym failed for %s: %s", drugbank_id, e)

        log.warning("[API] Could not map %s to ChEMBL", drugbank_id)
        return None