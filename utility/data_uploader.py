import io
import json

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