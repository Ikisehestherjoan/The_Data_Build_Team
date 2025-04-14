# Stock Price Data Engineering Pipeline
This is an end-to-end data engineering project that analyzes historical stock prices of three companies over multiple years. The project demonstrates the full data pipeline lifecycle—from data ingestion to visualization and alerting—using modern data engineering tools and best practices.

🔧 Key Features
API Integration: Retrieves historical stock data from the Alpha Vantage public API.

Object Storage: Stores raw data in MinIO (S3-compatible object storage).

Data Transformation: Cleans, curates, and transforms data into a structured format.

Database Storage: Loads processed data into a PostgreSQL database.

Visualization: Creates interactive dashboards in Power BI to track market trends.

Alert System: Sends email alerts for significant stock price changes and pipeline failures.

Containerization: Encapsulates the pipeline in a Docker container for portability.

Orchestration: Automates the entire workflow using Apache Airflow.

🚀 Tech Stack
Python

Alpha Vantage API

MinIO

PostgreSQL

Power BI

Docker

Apache Airflow

