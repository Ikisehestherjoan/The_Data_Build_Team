import io
import json
import pandas as pd

# Function to upload the json data to a minio bucket
def upload_to_minio(client,data,bucket_name,company_name, current_month):

    # Convert to bytes
    data_bytes = io.BytesIO(json.dumps(data, indent=2).encode("utf-8"))

    object_path = f"{bucket_name}/{company_name}/{current_month}"
    
    # Upload to MinIO
    client.put_object(
        bucket_name,
        object_path,
        data_bytes,
        length=len(data_bytes.getvalue()),
        content_type="application/json"
    )


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