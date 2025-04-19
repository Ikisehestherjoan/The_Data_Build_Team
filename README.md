# Stock Price Data Engineering Pipeline
![alt text](
<img
  src="https://github.com/Ikisehestherjoan/The_Data_Build_Team/blob/main/stock%20price%20pipeline%20architecture.jpeg"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
This project is an end-to-end data engineering and analytics pipeline that collects stock market data from a public API, cleans and transforms it, stores it in a PostgreSQL database, and visualizes insights using Power BI. It also includes an alert system to notify significant stock price changes or pipeline failures.

## Objective

- Collect stock market data for **IBM**, **Microsoft**, and **Apple** over a **5-year period**
- Analyze market trends
- Perform comparative analysis between the three companies
- Automate the entire data pipeline with email alerts for critical events


## Data Source

- **API**: [Alpha Vantage](https://www.alphavantage.co)


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
