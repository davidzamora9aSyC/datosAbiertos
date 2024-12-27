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

    print("Iniciando la descarga de datos...")

    while True:
        print(f"Consultando datos con offset {offset} y límite {limit}...")
        try:
            results = client.get(dataset_identifier, limit=limit, offset=offset)
            if not results:
                print("No hay más resultados para consultar.")
                break

            print(f"Se obtuvieron {len(results)} registros en esta iteración.")
            all_results.extend(results)
            offset += limit
        except Exception as e:
            print(f"Error durante la consulta: {e}. Intentando nuevamente en 5 segundos...")
            import time
            time.sleep(5)

    print(f"Se completó la consulta. Total de registros descargados: {len(all_results)}")
    return pd.DataFrame.from_records(all_results)

def main():
    print("Comenzando el proceso...")
    data = fetch_all_data(DOMAIN, DATASET_IDENTIFIER, LIMIT, APP_TOKEN)
    
    print(f"Total de registros final: {len(data)}")
    output_file = "rentabilidades_fic.csv"
    print(f"Guardando los datos en el archivo: {output_file}")
    data.to_csv(output_file, index=False)
    print("Datos guardados exitosamente.")

if __name__ == "__main__":
    main()
