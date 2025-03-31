import os
import requests
import csv

# Constants
CSV_FILENAME = "pokemon_data.csv"
PROGRESS_FILE = "progress.txt"

# Get the last fetched Pokémon index
def get_start_index():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    return 1  # Start from the first Pokémon

# Fetch Pokémon data from PokeAPI and append to CSV
def fetch_pokemon_data(start_index, end_index):
    file_exists = os.path.exists(CSV_FILENAME)
    
    with open(CSV_FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write headers if the file doesn't exist
        if not file_exists:
            writer.writerow(["ID", "Name", "Type(s)", "Height", "Weight", "Base XP", "Abilities"])

        # Fetch Pokémon data from PokeAPI
        for pokemon_id in range(start_index, end_index + 1):
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Extract relevant details
                name = data["name"].capitalize()
                types = ", ".join([t["type"]["name"] for t in data["types"]])
                height = data["height"]
                weight = data["weight"]
                base_xp = data["base_experience"]
                abilities = ", ".join([a["ability"]["name"] for a in data["abilities"]])

                # Append data to CSV
                writer.writerow([pokemon_id, name, types, height, weight, base_xp, abilities])
                print(f"✅ Retrieved data for {name} (ID {pokemon_id})")
            else:
                print(f"❌ Failed to fetch Pokémon ID {pokemon_id} (Error {response.status_code})")
    
    return end_index + 1  # Return next start index

# Save the next index to progress.txt
def save_progress(next_index):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(next_index))
    print(f"📄 Progress saved. Next batch starts from Pokémon {next_index}.")
