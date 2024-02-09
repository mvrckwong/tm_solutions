from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from config import *
from extract import main as EXTRACT_NAME


default_args = {
    'owner': 'Maverick Wong',
    'depends_on_past': True,
    'schedule_interval': None,
    
    'start_date': datetime(2024, 1, 1),
    'end_date': None,
    
    
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 3,
    # 'retry_delay': timedelta(minutes=5),
}
    
with DAG(
    '01_BigqueryExtraction',
    default_args=default_args,
    description='Extraction of data inside bigquery',
) as dag:
    
    # Define the task within the DAG context
    run_extraction = PythonOperator(
        task_id='run_extraction',
        python_callable=EXTRACT_NAME(test=True),
        #schedule_interval=None,
        dag=dag
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