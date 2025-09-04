import pandas as pd
from pathlib import Path

# Définir les chemins de base
DATA_DIR = Path("data")
CLEANED_DATA_DIR = DATA_DIR / "cleaned_data"
ENRICHED_DATA_DIR = DATA_DIR / "enriched_data"

def enrich_orders(df: pd.DataFrame) -> pd.DataFrame:
    # Exemple d'enrichissement : ajouter une colonne "revenue" si elle n'existe pas
    if "quantity" in df.columns and "price" in df.columns:
        df["revenue"] = df["quantity"] * df["price"]
    return df

def process_entity(entity: str, enrich_func):
    cleaned_entity_dir = CLEANED_DATA_DIR / entity
    enriched_entity_dir = ENRICHED_DATA_DIR / entity
    enriched_entity_dir.mkdir(parents=True, exist_ok=True)

    if not cleaned_entity_dir.exists():
        print(f"Aucun dossier trouvé pour {entity}")
        return

    for filepath in cleaned_entity_dir.rglob("*.csv"):
        try:
            df = pd.read_csv(filepath)
            df_enriched = enrich_func(df)

            relative_path = filepath.relative_to(cleaned_entity_dir)
            output_path = enriched_entity_dir / relative_path

            output_path.parent.mkdir(parents=True, exist_ok=True)

            df_enriched.to_csv(output_path, index=False)
            print(f"Fichier enrichi : {output_path}")
        except Exception as e:
            print(f"Erreur avec {filepath}: {e}")

if __name__ == "__main__":
    process_entity("orders", enrich_orders)
    print("Enrichissement terminé !")
