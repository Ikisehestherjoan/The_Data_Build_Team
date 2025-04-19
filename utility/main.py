from datetime import datetime
from dateutil.relativedelta import relativedelta
from utility.auxiliary import get_current_file,set_up_minio
from utility.extract_data import get_data

# Main function that combines all the steps
def get_stock_data(company_list, connection_str, access_key, secret_key, bucket_name, start_date, end_date):
    base_url = 'https://www.alphavantage.co/query'
    
    # Parse dates
    start = datetime.strptime(start_date, "%Y-%m")
    end = datetime.strptime(end_date, "%Y-%m")
    
    # Create a MinIO connection
    client = set_up_minio(connection_str, access_key, secret_key, bucket_name)

    # Get current data range if files already exist
    min_date, max_date = get_current_file(client, bucket_name)

    if min_date and max_date:

        # Convert tuples like (2023, 4) to datetime
        min_date_obj = datetime(min_date[0], min_date[1], 1) - relativedelta(months=1) # Exlude existing min file
        max_date_obj = datetime(max_date[0], max_date[1], 1)

        # Determine gaps before or after existing data
        if min_date_obj > start:
            new_end = min_date_obj.strftime("%Y-%m")
            for company_name in company_list:
                get_data(base_url, client, bucket_name, company_name, start_date, new_end)

        if max_date_obj < end:
            new_start = max_date_obj.strftime("%Y-%m")
            for company_name in company_list:
                get_data(base_url, client, bucket_name, company_name, new_start, end_date)

    else:
        # No file exists, get full range for all companies
        for company_name in company_list:
            get_data(base_url, client, bucket_name, company_name, start_date, end_date)