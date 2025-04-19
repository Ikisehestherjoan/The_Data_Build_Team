from dateutil.relativedelta import relativedelta
import requests
from datetime import datetime
from utility.data_loader import upload_to_minio


# Function to get data from the api and pass to Minio
def get_data(base_url, client, bucket_name, company_name, start_date, end_date):
    """
    Download data in 'YYYY-MM' format for each month between start_date and end_date (inclusive),
    and upload to MinIO.
    """
    try:
        # Parse dates
        start = datetime.strptime(start_date, "%Y-%m")
        end = datetime.strptime(end_date, "%Y-%m")
        
        if start > end:
            raise ValueError("Start date must be less than end date.")

        current = start
        while current <= end:
            current_month = current.strftime("%Y-%m")
            params = {
                'outputsize': 'full',
                'extended_hours': 'false',
                'apikey': 'IFBBUTAZ8NWO52MF',
                'interval': '60min',
                'function': 'TIME_SERIES_INTRADAY',
                'symbol': company_name,
                'month': current_month
            }

            response = requests.get(base_url, params=params)
            try:
                upload_to_minio(client, response.json(), bucket_name, company_name, current_month)
            except Exception as e:
                print(f"Upload failed for {current_month}: {e}")
            
            current += relativedelta(months=1)

    except Exception as e:
        print(f"Error: {e}")