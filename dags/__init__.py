from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator

schedule_interval = "30 16 * * *" 
dag = DAG(
    dag_id="daily_dag",
    default_args={
        "owner": "TY",
        "retry_delay": timedelta(minutes=5),
    },
    schedule_interval=schedule_interval,
    start_date=datetime(2022, 7, 20),
    catchup=False,
)

start = EmptyOperator(task_id=TaskId.start.init_task_id, dag=dag)
end = EmptyOperator(task_id=TaskId.backup_end.init_task_id, dag=dag)

start >> end



