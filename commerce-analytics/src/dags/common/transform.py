import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")  
RAW_DATA_DIR = DATA_DIR / "raw_data"
CLEANED_DATA_DIR = DATA_DIR / "cleaned_data"

def clean_clients(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["customer_id"])
    df = df.dropna()
    return df

def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["product_id"])
    df = df.dropna()
    return df

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["order_id"])
    df = df.dropna()
    return df

def process_entity(entity: str, cleaning_func):
    raw_entity_dir = RAW_DATA_DIR / entity
    cleaned_entity_dir = CLEANED_DATA_DIR / entity
    cleaned_entity_dir.mkdir(parents=True, exist_ok=True)

    if not raw_entity_dir.exists():
        print(f"Aucun dossier trouvé pour {entity}")
        return

    for filepath in raw_entity_dir.rglob("*.csv"):
        try:
            df = pd.read_csv(filepath)
            df_clean = cleaning_func(df)
            relative_path = filepath.relative_to(raw_entity_dir)  
            output_path = cleaned_entity_dir / relative_path  
            output_path.parent.mkdir(parents=True, exist_ok=True)
            df_clean.to_csv(output_path, index=False)
            print(f"Fichier nettoyé : {output_path}")
        except Exception as e:
            print(f"Erreur avec {filepath}: {e}")

if __name__ == "__main__":
    process_entity("clients", clean_clients)
    process_entity("products", clean_products)
    process_entity("orders", clean_orders)

    print("Transformation terminée !")
