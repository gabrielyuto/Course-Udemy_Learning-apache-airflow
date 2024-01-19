from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('pool', description="variaveispool",
          schedule_interval=None, start_date=datetime(2024,1,15),
          catchup=False)

task1 = BashOperator(task_id="tsk_1", bash_command="sleep 5", dag=dag, pool="meupool")
task2 = BashOperator(task_id="tsk_2", bash_command="sleep 5", dag=dag, pool="meupool", priority_weight=5)
task3 = BashOperator(task_id="tsk_3", bash_command="sleep 5", dag=dag, pool="meupool")
task4 = BashOperator(task_id="tsk_4", bash_command="sleep 5", dag=dag, pool="meupool", priority_weight=10)
