from datetime import timedelta
from email.policy import default
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from pendulum import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,1,29),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'asdag',
    default_args=default_args,
    description='A simple songs DAG',
    schedule_interval=timedelta(days=1),
)

def fuction():
    print("Showing  something")

run_etl = PythonOperator(
    task_id='spotify_etl',
    python_callable=fuction,
    dag=dag,
)    

run_etl