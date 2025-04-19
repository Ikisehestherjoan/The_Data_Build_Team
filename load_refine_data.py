from utility.auxiliary import set_up_minio
from utility.data_loader import load_data
from sqlalchemy import create_engine, inspect

# Function to load the data into Postgres
def update_postgres(client, bucket_name, db_username,db_password,db_connection_str,db_name):
    
    # Load the data from the Minio bucket
    df = load_data(client, bucket_name)

    # PostgreSQL connection string
    engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_connection_str}/{db_name}")

    # Check if table exists
    inspector = inspect(engine)
    if 'stock_data' not in inspector.get_table_names():
        # Create the table by writing the DataFrame with 'replace'
        df.to_sql('stock_data', engine, if_exists='replace', index=False)

    # Now append the data
    df.to_sql('stock_data', engine, if_exists='append', index=False)

if __name__=="__main__":
    access_key="mariam"
    secret_key="mariam123"
    bucket_name = "stock-rawdata"
    connection_str = "localhost:9000"
    db_username="mariam"
    db_password="mariam123"
    db_connection_str="localhost:5432"
    db_name="mydb"
    client = set_up_minio(connection_str, access_key, secret_key, bucket_name)
    update_postgres(client, bucket_name, db_username,db_password,db_connection_str,db_name)



