# Data Ingestion Pipeline

This project demonstrates a simple **Data Ingestion Pipeline** built over a weekend using an **API** to extract data, store it in **BigQuery**, and automate the process using **Windows Task Scheduler**.

## Project Overview

The pipeline performs the following steps:

1. **Data Extraction**: Data is pulled from an API (free version, with a 10-record limit per request).
2. **Local Storage**: The data is saved locally as a **CSV file**.
3. **BigQuery Integration**: The extracted data is simultaneously uploaded to a **BigQuery dataset → table**, ensuring no duplicates.
4. **Automation**: The process is automated to run **daily** using **Windows Task Scheduler**.

## Features

- **Data Correctness**: Ensures data integrity with no duplicate entries.
- **Automation**: Fully automated process that runs daily.
- **Simple Integration**: Easy setup to get started with data ingestion and automation.

## Requirements

- Python (or another suitable language) for API handling and file operations.
- **BigQuery** account and API access.
- **Windows** machine for Task Scheduler automation.

## Setting Up Google Credentials

To authenticate and interact with Google Cloud services (like BigQuery), you'll need to set up Google Cloud credentials. Follow these steps to create your credentials:

1. **Go to the Google Cloud Console**:
   - Visit [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a Project**:
   - In the console, click on the **project dropdown** and select **Create Project**.
   - Name your project and click **Create**.

3. **Enable BigQuery API**:
   - In the **APIs & Services** dashboard, click on **Enable APIs and Services**.
   - Search for **BigQuery API** and click **Enable**.

4. **Create Service Account**:
   - Go to the **IAM & Admin** section and select **Service Accounts**.
   - Click **Create Service Account**.
   - Provide a name, such as "data-ingestion-service-account".
   - Grant the role **Project > Owner** (or the necessary permissions for BigQuery).
   - Click **Continue** and **Done**.

5. **Download the Service Account Key**:
   - In the **Service Accounts** section, find your created service account.
   - Click on the three vertical dots beside it and select **Create Key**.
   - Choose **JSON** format and click **Create**. This will download a file containing your Google credentials.

6. **Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable**:
   - Store the downloaded JSON file in a safe location (e.g., `C:\path\to\your\credentials.json`).
   - Set the environment variable on your system:
     - On **Windows**, open Command Prompt and run:
       ```bash
       set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\credentials.json
       ```
     - On **Linux/Mac**, run:
       ```bash
       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
       ```

This will allow your application to authenticate and interact with Google Cloud services.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/manans791/Data_Ingestion.git
