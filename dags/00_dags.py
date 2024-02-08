import importlib
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from config import *

extract_module = importlib.import_module('01_extract')
extract_main = extract_module.test

default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Sample DAG
with DAG(
    '01_Extraction',
    default_args=default_args,
    description='Extraction of data inside bigquery',
    schedule_interval=timedelta(days=1),
) as dag:
    
    # Define the task within the DAG context
    run_extraction = PythonOperator(
        task_id='run_extraction',
        python_callable=extract_main,
    )


# with DAG(
#     f"{current_proj_name}-Batch_Mapping",
#     default_args = AIRFLOW_CONFIG.DEFAULT_ARGS,
#     schedule_interval = None,
#     on_success_callback = on_success,
#     on_failure_callback=on_failure,
#     catchup = False,
    
#     description = "Batch process that runs all necessary processes for the loadsheet.",
# ) as dag:
    
#     run_title = "batch_loadsheet"
    
#     # Run the python using bash operator
#     run_combine = BashOperator(task_id=f"{run_title}-combine",
#                                on_failure_callback=on_failure,
#                                on_retry_callback=on_retry,
#                                bash_command = "python " + \
#                                    str(current_proj_apps / "A0130_Combine.py"), 
#                                dag=dag)
    
#     # Run the python using bash operator
#     run_create = BashOperator(task_id=f"{run_title}-create",
#                                on_failure_callback=on_failure,
#                                on_retry_callback=on_retry,
#                                bash_command = "python " + \
#                                    str(current_proj_apps / "A0131_Create.py"), 
#                                dag=dag)
    
#     # Run the python using bash operator
#     run_mapping = BashOperator(task_id=f"{run_title}-mapping",
#                                on_failure_callback=on_failure,
#                                on_retry_callback=on_retry,
#                                bash_command = "python " + \
#                                    str(current_proj_apps / "A0185_Map.py"),
#                                dag=dag)
    
    
#     # Define task dependencies if any
#     run_combine >> run_create >> run_mapping