
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_ding():
    return 'Ding Dong World'
    
def second_task_callable():
    return 'Second hello'

def third_task_callable():
    return 'Third hello'


hello_operator = PythonOperator(
    task_id='ding_task', 
    python_callable=print_ding, 
    dag=dag)

second_operator = PythonOperator(
    task_id='second_task', 
    python_callable=second_task_callable, 
    dag=dag)
third_operator = PythonOperator(
    task_id='third_task', 
    python_callable=third_task_callable, 
    dag=dag)


with DAG('automated_sample_task_dag_2021_01_10', description='Second sample dag created by script',
          schedule_interval='* * 0 2',
          start_date=datetime(2021-10-24), catchup=True) as dag:

hello_operator >> second_operator >> third_operator

