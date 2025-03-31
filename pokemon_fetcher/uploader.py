import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Set the path to your service account key file
SERVICE_ACCOUNT_FILE = r"F:\project\pokemons-455012-175f0c65518c.json"

# Load credentials explicitly
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Initialize BigQuery Client with explicit credentials
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Google Cloud configurations
PROJECT_ID = "pokemons-455012"
DATASET_ID = "Pokemon_Master"
TABLE_ID = "Master_Data"

def upload_to_bigquery(csv_filename):
    """
    Uploads the given CSV file to BigQuery.
    """
    table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    try:
        # Read CSV into Pandas DataFrame
        df = pd.read_csv(csv_filename)

        # Remove duplicates before uploading
        df.drop_duplicates(subset=["ID"], inplace=True)

        # Define BigQuery Schema
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("ID", "INTEGER"),
                bigquery.SchemaField("Name", "STRING"),
                bigquery.SchemaField("Type", "STRING"),
                bigquery.SchemaField("Height", "INTEGER"),
                bigquery.SchemaField("Weight", "INTEGER"),
                bigquery.SchemaField("Base XP", "INTEGER"),
                bigquery.SchemaField("Abilities", "STRING"),
            ],
            write_disposition="WRITE_TRUNCATE",  # Overwrites existing data
        )

        # Load DataFrame into BigQuery
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result(timeout=60)  # Wait for the job to complete

        print(f"🚀 Data successfully uploaded to BigQuery table {table_id}!")

    except Exception as e:
        print(f"❌ Failed to upload to BigQuery: {e}")
