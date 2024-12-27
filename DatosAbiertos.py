from sodapy import Socrata
import pandas as pd

# Configuración
DOMAIN = "www.datos.gov.co"
DATASET_IDENTIFIER = "qhpu-8ixx"
LIMIT = 1000
APP_TOKEN = "9TQ0tB29FISsC5B3kXlEllXET"  # Reemplaza con tu App Token

def fetch_all_data(domain, dataset_identifier, limit=1000, app_token=None):
    client = Socrata(domain, app_token, timeout=60)
    offset = 0
    all_results = []

    while True:
        results = client.get(dataset_identifier, limit=limit, offset=offset)
        if not results:
            break

        all_results.extend(results)
        offset += limit

    return pd.DataFrame.from_records(all_results)

def main():
    print("Fetching data...")
    data = fetch_all_data(DOMAIN, DATASET_IDENTIFIER, LIMIT, APP_TOKEN)
    print(f"Fetched {len(data)} records.")

    # Guarda los datos en un archivo CSV
    output_file = "rentabilidades_fic.csv"
    data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
