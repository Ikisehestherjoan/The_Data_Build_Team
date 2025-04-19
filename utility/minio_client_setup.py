from minio import Minio

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