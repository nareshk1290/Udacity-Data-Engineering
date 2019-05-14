import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")


def addition():
    logging.info(f"2 + 2 = {2+2}")


def subtraction():
    logging.info(f"6 -2 = {6-2}")


def division():
    logging.info(f"10 / 2 = {int(10/2)}")
 
def completed_task():
    logging.info("All Tasks Completed")


dag = DAG(
    "lesson1.exercise3",
    schedule_interval='@hourly',
    start_date=datetime.datetime.now() - datetime.timedelta(days=1))

hello_world_task = PythonOperator(
    task_id="hello_world",
    python_callable=hello_world,
    dag=dag)

addition_task = PythonOperator(
    task_id="addition",
    python_callable=addition,
    dag=dag)

subraction_task = PythonOperator(
    task_id="subtraction",
    python_callable=subtraction,
    dag=dag)

division_task = PythonOperator(
    task_id="division",
    python_callable=division,
    dag=dag)

completed_task = PythonOperator(
    task_id="completed_task",
    python_callable=completed_task,
    dag=dag)
#
#                    ->  addition_task
#                   /                 \
# hello_world_task  -> division_task-> completed_task                
#                   \                 /
#                    -> subtraction_task

hello_world_task >> addition_task
hello_world_task >> division_task
hello_world_task >> subtraction_task
addition_task >> completed_task
division_task >> completed_task
subtraction_task >> completed_task