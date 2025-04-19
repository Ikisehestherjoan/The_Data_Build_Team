# Building an End-to-End Data Pipeline for Stock Price Analysis

This project is an end-to-end data engineering and analytics pipeline that collects stock market data from a public API, cleans and transforms it, stores it in a PostgreSQL database, and visualizes insights using Power BI. It also includes an alert system to notify significant stock price changes or pipeline failures.

## Objective

- Collect stock market data for **IBM**, **Microsoft**, and **Apple** over a **5-year period**
- Analyze market trends
- Perform comparative analysis between the three companies
- Automate the entire data pipeline with email alerts for critical events


## Data Source

- **API**: [Alpha Vantage](https://www.alphavantage.co)

## End to End Stock price Data Engineering Pipeline

<img
  src="https://github.com/Ikisehestherjoan/The_Data_Build_Team/blob/main/stock%20price%20pipeline%20architecture.jpeg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">


## Key Features
**API Integration**: Retrieves historical stock data from the Alpha Vantage public API.

**Object Storage**: Stores raw data in MinIO (S3-compatible object storage).

**Data Transformation**: Cleans, curates, and transforms data into a structured format.

**Database Storage**: Loads processed data into a PostgreSQL database.

**Visualization**: Creates interactive dashboards in Power BI to track market trends.

**Alert System**: Sends email alerts for significant stock price changes and pipeline failures.

**Containerization**: Encapsulates the pipeline in a Docker container for portability.

**Orchestration**: Automates the entire workflow using Apache Airflow.

## Tech Stack
|Tool            | Purpose|
| ------         | -------|
| Python         | For data extraction, cleaning, and transformation|
| PostgreSQL     | To store processed data|
| MinIO          |For storing raw data in object format |
| Docker         |  To containerize and simplify deployment|
| Apache Airflow   |For orchestrating and scheduling pipeline tasks|
|Power BI        | For visualizing market trends|
|GitHub            | For version control and collaboration |



### 🚀 How to Set Up & Run the Project

Once the project is pushed to GitHub, setting it up to run on your local machine or server involves several steps. Here's a detailed guide for anyone who wants to replicate the project:

---

#### **1. Clone the GitHub Repository**
First, you'll need to clone the repository to your local machine using Git. Open your terminal and run the following command:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

#### **2. Set Up Python Environment**
This project relies on Python for data extraction, cleaning, and transformation. It's a good idea to create a virtual environment to keep dependencies organized. Run these commands:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

The `requirements.txt` file should contain all the necessary libraries like `pandas`, `requests`, `sqlalchemy`, etc.

---

#### **3. Docker Setup for MinIO**
If you haven’t used MinIO before, we recommend setting it up using Docker. MinIO will store the raw data. Here’s how to run it locally:

```bash
# Pull the MinIO Docker image
docker pull minio/minio

# Run MinIO container (this will run MinIO locally on port 9000)
docker run -p 9000:9000 -e "MINIO_ACCESS_KEY=minioadmin" -e "MINIO_SECRET_KEY=minioadmin" minio/minio server /data
```

After running this, you can access the MinIO web interface at `http://localhost:9000` using the credentials `minioadmin:minioadmin`.

---

#### **4. PostgreSQL Setup**
Next, set up a PostgreSQL database where the processed data will be stored. You can use Docker to run a PostgreSQL container:

```bash
# Pull the PostgreSQL Docker image
docker pull postgres

# Run PostgreSQL container (this will run PostgreSQL locally on port 5432)
docker run -p 5432:5432 -e POSTGRES_PASSWORD=yourpassword -e POSTGRES_DB=financial_data postgres
```

You can connect to the PostgreSQL database using a tool like **pgAdmin** or **psql** to ensure the setup is correct.

---

#### **5. Apache Airflow Setup**
Apache Airflow is used for orchestration and scheduling. Set up Airflow on your local machine or a server. For local setups:

```bash
# Install Apache Airflow
pip install apache-airflow

# Initialize the Airflow database
airflow db init

# Start the Airflow web server
airflow webserver --port 8080

# Start the Airflow scheduler in another terminal window
airflow scheduler
```

Visit `http://localhost:8080` to access the Airflow web UI.

---

#### **6. Configuring API Keys**
To fetch stock data from Alpha Vantage, you will need an API key. Sign up for a free account on [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and get your key. Once you have it, store it in an `.env` file for security and load it in your Python scripts using `python-dotenv`.

Example `.env` file:

```
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

---

#### **7. Running the Pipeline**
Once all dependencies are installed and your environment is set up, you can run the entire pipeline using Apache Airflow or manually through Python scripts.

To manually run the data extraction and loading, you can execute:

```bash
python extract_data.py  # Pulls data from Alpha Vantage
python transform_data.py  # Cleans and transforms data
python load_data.py  # Loads data into PostgreSQL
```

If you prefer to use Airflow, trigger the appropriate DAG from the Airflow UI to automate the process.

---

#### **8. Visualizing the Data**
Once the data is loaded into PostgreSQL, you can use **Power BI** or other visualization tools to create interactive dashboards. Connect Power BI to the PostgreSQL database using the PostgreSQL connector, and query the relevant data to build your visualizations.

---

#### **9. Troubleshooting**
- If you encounter errors with **MinIO** or **PostgreSQL**, check the container logs for any issues.
- If there are issues with **API limits** from Alpha Vantage, try spreading out the requests over multiple days or use multiple API keys.

---

### 🔄 Final Notes
After following these steps, you should have the entire pipeline running locally. You can modify the DAGs in Airflow, tweak the transformation logic in Python, or create custom dashboards in Power BI.

Feel free to fork the repository, contribute to the project, or reach out if you encounter any issues!

---

## Kindly read up on 
** Link to medium article:**
