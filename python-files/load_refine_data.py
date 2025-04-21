import os
from utility.auxiliary import set_up_minio
from utility.data_loader import load_data
from sqlalchemy import create_engine, inspect

# Function to load the data into Postgres
def update_postgres(client, bucket_name, db_username,db_password,db_connection_str,db_name):
    
    # Load the data from the Minio bucket
    df = load_data(client, bucket_name)

    # PostgreSQL connection string
    engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_connection_str}/{db_name}")

    # Create the table by writing the DataFrame with 'replace'
    df.to_sql('stock_data', engine, if_exists='replace', index=False)

if __name__=="__main__":
    access_key= os.getenv("STM_ACCESS_KEY")
    secret_key= os.getenv("STM_SECRET_KEY")
    bucket_name = "stock-rawdata"
    connection_str = os.getenv("MINIO_CONNECTION_STRING")
    db_username= os.getenv("STM_ACCESS_KEY")
    db_password= os.getenv("STM_SECRET_KEY")
    db_connection_str= os.getenv("POSTGRES_CONNECTION_STRING")
    db_name= "mydb"
    client = set_up_minio(connection_str, access_key, secret_key, bucket_name)
    update_postgres(client, bucket_name, db_username,db_password,db_connection_str,db_name)



