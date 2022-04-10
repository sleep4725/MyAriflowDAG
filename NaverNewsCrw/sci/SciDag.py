"""_summary_
@filename : sample.py
@author : JunHyeon.Kim
"""
import pendulum
from datetime import datetime

from airflow.operators.python_operator import PythonOperator
from airflow import DAG

local_tz = pendulum.timezone("Asia/Seoul")
### argument define 
default_args = {
    'owner'           : 'JunHyeon.Kim',
    'depends_on_past' : False,
    'email'           : ['sleep4725@naver.com'],
    'email_on_failure': True,
    'email_on_retry'  : False,
    'retires'         : 3,
    'start_date'      : datetime(2022, 4, 10, 17, lzinfo=local_tz)
}

def cllct_run():
    
    pass  

### DAG define 
with DAG(
    dag_id = 'NaverNewsCllct',
    default_args = default_args,
    schedule_interval = timedelta(minutes = 5),
    start_date = datetime(2021, 10, 22),
    catchup = False,
    tags = ['Sample']
) as dag:
    t1 = PythonOperator(task_id='task_1',
                    provide_context=True,
                    python_callable=cllct_run,
                    dag=dag)
    
    t1 