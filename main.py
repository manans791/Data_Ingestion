import time
from pokemon_fetcher.fetcher import fetch_pokemon_data, get_start_index, save_progress
from pokemon_fetcher.uploader import upload_to_bigquery
import sys


def main():
    start_index = get_start_index()
    end_index = start_index + 9
    
    # Fetch and save Pokémon data to CSV
    next_index = fetch_pokemon_data(start_index, end_index)
    save_progress(next_index)
    
    # Upload the data to BigQuery
    upload_to_bigquery("pokemon_data.csv")
    sys.exit(0)

if __name__ == "__main__":
        main()
        
        # Sleep for 5 hours before running again
        time.sleep(5 * 60 * 60)  # 5 hours
