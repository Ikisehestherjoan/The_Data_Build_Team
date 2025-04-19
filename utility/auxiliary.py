import os
from minio import Minio
import pandas as pd
import json

# This return the maximum and minimum date of the existing/historical data
def get_current_file(client,bucket_name):

    # list out all the files in the bucket
    objects = client.list_objects(bucket_name,recursive=True)

    # Extract the file names
    file_names = [ os.path.basename(obj.object_name).split('.')[0] for obj in objects]

    # convert file name to a tuple (year,month)
    parsed_elements = [tuple(map(int,item.split('-'))) for item in file_names]

    # Return min and max (Year, month)
    if not parsed_elements or not parsed_elements:
        return ([],[])
    return min(parsed_elements),max(parsed_elements)

# Function to set up minio
def set_up_minio(connection_str,access_key,secret_key, bucket_name):
    client = Minio(
        connection_str,
        access_key=access_key,
        secret_key=secret_key,
        secure=False
    )

    # Ensure bucket exists
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    return client

# Function to load data from minio and convert to dataframe, with some transformations
def load_data(client, bucket_name):
    data_list = []
    
    # List all files in the bucket
    objects = client.list_objects(bucket_name, recursive=True)
    
    for obj in objects:
        obj_data = client.get_object(bucket_name, obj.object_name)
        file_content = obj_data.read()  # Read byte content
        
        # Convert to dict
        json_data = json.loads(file_content.decode("utf-8"))

        if "Time Series (60min)" in json_data and "Meta Data" in json_data:
            df = pd.DataFrame(json_data['Time Series (60min)']).T.reset_index()
            df['company'] = json_data['Meta Data']['2. Symbol']
            data_list.append(df)

    if not data_list:
        return pd.DataFrame()  # Return empty DF if nothing was loaded
    
    result_df = pd.concat(data_list, ignore_index=True)
    result_df.rename(columns={
        'index': 'date',
        '1. open': 'open_price',
        '2. high': 'high_price',
        '3. low': 'low_price',
        '4. close': 'close_price',
        '5. volume': 'volume'
    }, inplace=True)
    
    return result_df