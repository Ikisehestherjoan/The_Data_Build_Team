from utility.main import get_stock_data
from datetime import datetime

if __name__== "__main__":
    company_list = ['AAPL', 'IBM', 'MSFT']
    connection_str = "localhost:9000"
    access_key="mariam"
    secret_key="mariam123"
    bucket_name = "stock-rawdata"
    start_date = '2023-01'
    end_date = datetime.now().strftime("%Y-%m")
    get_stock_data(company_list, connection_str, access_key, secret_key, bucket_name, start_date, end_date)
