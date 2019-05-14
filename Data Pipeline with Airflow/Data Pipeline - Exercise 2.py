import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def second_prog():
    logging.info("This is my second program for airflow")

dag = DAG(
        "lesson1.exercise2",
        start_date=datetime.datetime.now() - datetime.timedelta(days=2),
        schedule_interval="@daily")

task = PythonOperator(
        task_id="exercise_2",
        python_callable=second_prog,
        dag=dag)
