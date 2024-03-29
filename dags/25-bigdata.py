from airflow import DAG
from datetime import datetime
from big_data_operator import BigDataOperator

dag = DAG('bigdata', description="Nossa Dag",
          schedule_interval=None, start_date=datetime(2024,1,22),
          catchup=False)

big_data = BigDataOperator(
        task_id = "big_data",
        path_to_csv_file = '/opt/airflow/data/Churn.csv',
        path_to_save_file = '/opt/airflow/data/Churn.parquet',
        file_type = 'parquet',
        dag = dag
        )

big_data
