import os
from minio import Minio

# This return the maximum and minimum date of the existing/historical data
def get_current_file(client, bucket_name,company_name):
    """
    Return the earliest and latest (year, month) tuple from filenames in a MinIO bucket,
    filtering out files smaller than 1KB.
    """

    parsed_elements = []

    # List objects in the bucket
    for obj in client.list_objects(bucket_name, prefix=f"{bucket_name}/{company_name}/",recursive=True):
        try:
            # Check size
            if client.stat_object(bucket_name, obj.object_name).size / 1024 > 1:

                # Extract base filename without extension
                base_name = os.path.basename(obj.object_name).split('.')[0]
                
                # Parse year and month
                parsed = tuple(map(int, base_name.split('-')))
                parsed_elements.append(parsed)

        except Exception as e:
            print(f"Skipping file {obj.object_name}: {e}")

    if not parsed_elements:
        return ([], [])

    return min(parsed_elements), max(parsed_elements)


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