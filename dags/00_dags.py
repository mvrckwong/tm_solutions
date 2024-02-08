from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from config import *

# Sample DAG
# with DAG(
#     f"{current_proj_name}-Preprocess_AssetReg",
#     default_args = AIRFLOW_CONFIG.DEFAULT_ARGS,
#     schedule_interval = AIRFLOW_CONFIG.SCHEDULE_INTERVAL
# ) as dag:
    
#     run_preprocess = BashOperator(task_id=f"run_preprocess",
#                                   on_failure_callback=on_failure,
#                                   on_retry_callback=on_retry,
#                                   bash_command = "python " + \
#                                     str(current_proj_pprocess / "main.py"), 
#                                   dag=dag)


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