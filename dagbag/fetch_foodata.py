
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello World'
    
def second_task_callable():
    return 'Second hello'

def third_task_callable():
    return 'Third hello'


hello_operator = PythonOperator(
    task_id='hello_task', 
    python_callable=print_hello, 
    dag=dag)

second_operator = PythonOperator(
    task_id='second_task', 
    python_callable=second_task_callable, 
    dag=dag)
third_operator = PythonOperator(
    task_id='third_task', 
    python_callable=third_task_callable, 
    dag=dag)


with DAG('automated_sample_task_dag_2021', description='Sample dag created by script',
          schedule_interval='* * 0 21',
          start_date=datetime(2021-10-21), catchup=True) as dag:

hello_operator >> second_operator >> third_operator

