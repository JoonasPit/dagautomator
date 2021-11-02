dagbase = """
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def {hello_op_callable}():
    return '{message_sample}'
    
def {second_op_callable}():
    return '{second_message}'

def {third_op_callable}():
    return '{third_message}'


hello_operator = PythonOperator(
    task_id='{hello_task_id}', 
    python_callable={hello_op_callable}, 
    dag=dag)

second_operator = PythonOperator(
    task_id='{second_task_id}', 
    python_callable={second_op_callable}, 
    dag=dag)
third_operator = PythonOperator(
    task_id='{third_task_id}', 
    python_callable={third_op_callable}, 
    dag=dag)


with DAG('{task_name}', description='{dag_description}',
          schedule_interval='{schedule_interval}',
          start_date=datetime({start_date}), catchup={catch_up}) as dag:

hello_operator >> second_operator >> third_operator

"""