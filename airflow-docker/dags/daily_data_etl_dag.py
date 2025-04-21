from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_python_scripts():
    # Assuming the python scripts are in the /app directory in the python container
    subprocess.run(["docker", "exec", "pythonapp", "python", "/app/extract_rawdata.py"], check = True)
    subprocess.run(["docker", "exec", "pythonapp", "python", "/app/load_refine_data.py"], check=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past':False,
    'start_date': datetime(2025, 4, 20),
    'retries': 1,
}

dag = DAG(
    'python_task_dag',
    default_args=default_args,
    description='A simple DAG to run Python scripts in the Python container',
    schedule_interval='0 8 * * *',  # Set to None for manual triggering or cron expression for scheduled runs
)

run_python_task = PythonOperator(
    task_id='run_python_scripts',
    python_callable=run_python_scripts,
    dag=dag,
)

run_python_task
