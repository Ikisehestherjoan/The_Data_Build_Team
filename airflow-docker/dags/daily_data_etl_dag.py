from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_python_extract():
    
    subprocess.run(["docker", "exec", "pythonapp", "python", "/app/extract_rawdata.py"], check = True)

def run_python_load():
    
    subprocess.run(["docker", "exec", "pythonapp", "python", "/app/load_refine_data.py"], check=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past':False,
    'start_date': datetime(2025, 4, 20),
    'retries': 1,
}

with DAG(
    'python_task_dag',
    default_args=default_args,
    description='A simple DAG to run Python scripts in the Python container',
    schedule_interval='0 8 * * *',  # Set to None for manual triggering or cron expression for scheduled runs
    catchup = False
) as dag:
    # Task to extract from api
    run_python_extract = PythonOperator(
        task_id='run_python_extract',
        python_callable=run_python_extract,
        dag=dag,
    )
    # Task to transform and load to postgres
    run_python_load = PythonOperator(
        task_id='run_python_load',
        python_callable=run_python_load,
        dag=dag,
    )


    # Define task dependencies

    run_python_extract >> run_python_load



