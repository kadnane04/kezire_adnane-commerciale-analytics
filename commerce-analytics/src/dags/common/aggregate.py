import pandas as pd
from pathlib import Path

# Définir les chemins de base
DATA_DIR = Path("data")
CLEANED_CLIENTS_DIR = DATA_DIR / "cleaned_data" / "clients"
CLEANED_PRODUCTS_DIR = DATA_DIR / "cleaned_data" / "products"
ENRICHED_ORDERS_DIR = DATA_DIR / "enriched_data" / "orders"

AGGREGATED_DIR = DATA_DIR / "aggregated_data"
DAILY_DIR = AGGREGATED_DIR / "daily"
MONTHLY_DIR = AGGREGATED_DIR / "monthly"

def aggregate_daily_clients():
    output_dir = DAILY_DIR / "clients"
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in CLEANED_CLIENTS_DIR.rglob("*.csv"):
        df = pd.read_csv(file)
        nb_clients = df["customer_id"].nunique()
        agg_df = pd.DataFrame({"date": [df["date"].iloc[0]], "nb_clients": [nb_clients]})

        relative_path = file.relative_to(CLEANED_CLIENTS_DIR)
        output_path = output_dir / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        agg_df.to_csv(output_path, index=False)
        print(f"Clients agrégés : {output_path}")

def aggregate_daily_products():
    output_dir = DAILY_DIR / "products"
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in CLEANED_PRODUCTS_DIR.rglob("*.csv"):
        df = pd.read_csv(file)
        total_stock = df["stock"].sum()
        agg_df = pd.DataFrame({"date": [df["date"].iloc[0]], "total_stock": [total_stock]})

        relative_path = file.relative_to(CLEANED_PRODUCTS_DIR)
        output_path = output_dir / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        agg_df.to_csv(output_path, index=False)
        print(f"Stock agrégé : {output_path}")

def aggregate_monthly_orders():
    output_dir = MONTHLY_DIR / "orders"
    output_dir.mkdir(parents=True, exist_ok=True)

    for year_dir in ENRICHED_ORDERS_DIR.iterdir():
        if not year_dir.is_dir():
            continue
        for month_dir in year_dir.iterdir():
            if not month_dir.is_dir():
                continue
            monthly_files = list(month_dir.glob("*.csv"))
            if not monthly_files:
                continue
            # concaténer toutes les commandes du mois
            df_list = [pd.read_csv(f) for f in monthly_files]
            month_df = pd.concat(df_list, ignore_index=True)
            revenue_total = month_df["revenue"].sum()
            month_str = f"{year_dir.name}-{month_dir.name}"
            agg_df = pd.DataFrame({"month": [month_str], "revenue": [revenue_total]})

            output_path = output_dir / f"{month_str}.csv"
            agg_df.to_csv(output_path, index=False)
            print(f"CA mensuel agrégé : {output_path}")

if __name__ == "__main__":
    aggregate_daily_clients()
    aggregate_daily_products()
    aggregate_monthly_orders()
    print("Agrégation terminée !")
