import pandas as pd
from sodapy import Socrata

# Configuración
DOMAIN = "www.datos.gov.co"
DATASET_IDENTIFIER = "qhpu-8ixx"
LIMIT = 1000  # Número máximo de registros por consulta

def fetch_all_data(domain, dataset_identifier, limit=1000):
    client = Socrata(domain, None)  # Cliente no autenticado
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
    data = fetch_all_data(DOMAIN, DATASET_IDENTIFIER, LIMIT)
    print(f"Fetched {len(data)} records.")

    # Guarda los datos en un archivo CSV
    output_file = "rentabilidades_fic.csv"
    data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
