# Building an End-to-End Data Pipeline for Stock Price Analysis

This project is an end-to-end data engineering and analytics pipeline that collects stock market data from a public API, cleans and transforms it, stores it in a PostgreSQL database, and visualizes insights using Power BI.

## Objective

- Collect stock market data for **IBM**, **Microsoft**, and **Apple** over a **2-year+ period**
- Analyze market trends
- Perform comparative analysis between the three companies
- Automate the entire data pipeline

## Data Source

- **API**: [Alpha Vantage](https://www.alphavantage.co)

## End to End Stock price Data Engineering Pipeline

<img
  src="https://github.com/Ikisehestherjoan/The_Data_Build_Team/blob/master/data_architecture.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">

  


## Key Features
**API Integration**: Retrieves historical stock data from the Alpha Vantage public API.

**Object Storage**: Stores raw data in MinIO (S3-compatible object storage).

**Data Transformation**: Cleans, curates, and transforms data into a structured format.

**Database Storage**: Loads processed data into a PostgreSQL database.

**Visualization**: Creates interactive dashboards in Power BI to track market trends.

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

---

#### **1. Clone the GitHub Repository**
First, you'll need to clone the repository to your local machine using Git. Open your terminal and run the following command:

```bash
git clone https://github.com/Ikisehestherjoan/The_Data_Build_Team.git
cd The_Data_Build_Team
```

#### **2. Create a .env file with the following variables**

```bash
ALPHA_VANTAGE_API_KEY=your_api_key_here
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
MINIO_ROOT_USER=miniouser
MINIO_ROOT_PASSWORD=miniopassword
STM_ACCESS_KEY=userxxxxx
STM_SECRET_KEY=xxxxx123
_AIRFLOW_WWW_USER_USERNAME=userxxxxx
_AIRFLOW_WWW_USER_PASSWORD=xxxxx123
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:yourpassword@mypostgres:5432/mydb

```

#### **3. Run Docker Compose Build to Setup the Required Services**

```bash
# creates MinIO, Postgres, Airflow and custom python services
docker-compose -f docker-compose.yml up --build -d

```
#### **4. Apache Airflow Setup Initialize**

```bash
# Apache Airflow Setup Initialize and start Airflow

airflow db init
airflow webserver &
airflow scheduler &

```

After running this, you can access the MinIO web interface at `http://localhost:9001` using the credentials created in the `.env` file


---

#### **5. Running the Pipeline**
Once your environment is set up, the pipeline has been scheduled to run everyday at 8am. You can run the entire pipeline manually using Apache Airflow webserver or manually through Python scripts.

To manually run the data extraction and loading, you can execute:

```bash
docker exec -it pythonapp python extract_rawdata.py  # extract data from Alpha Vantage and store in MinIO
docker exec -it pythonapp python load_refine_data.py  # transform the data and Load into PostgreSQL
```

If you prefer to use Airflow webserver, trigger the appropriate DAG from the Airflow UI to automate the process.
The name of the dag is 'python_task_dag'


#### **6. Visualizing the Data**
Once the data is loaded into PostgreSQL, you can use **Power BI** or other visualization tools to create interactive dashboards. Connect Power BI to the PostgreSQL database using the PostgreSQL connector provided in the `.env` file, and query the stock_data table to build your visualizations.

---

#### **7. Troubleshooting**
- If you encounter errors with **MinIO**, check the container logs for any issues.
  ```bash
  docker logs airflow  # check airflow logs 

If there are issues with **API limits** from Alpha Vantage, try spreading out the requests over multiple days or use multiple API keys.



### 🔄 Final Notes
After following these steps, you should have the entire pipeline running locally. You can modify the DAGs in Airflow, tweak the transformation logic in Python, or create custom dashboards in Power BI.

Feel free to fork the repository, contribute to the project, or reach out if you encounter any issues!

* **https://github.com/Titilopemigift**
* **https://github.com/motunrayom**
* **https://github.com/Ikisehestherjoan**
* **https://github.com/Data-dv**


## **Kindly read up on:
[Link to medium article](https://medium.com/@ikisehestherjoan/building-an-end-to-end-data-pipeline-for-stock-price-analysis-877fb14d948d)
