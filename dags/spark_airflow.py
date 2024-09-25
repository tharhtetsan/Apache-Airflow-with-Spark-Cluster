import airflow
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator



dag = DAG("spark_airflow", start_date=airflow.utils.dates.days_ago(1), 
        description="This is Spark Airflow testing", tags=["spark"],
        schedule='@daily',catchup=False )


start = PythonOperator(
    task_id = "start", 
    python_callable = lambda : print("Jobs started"),
    dag= dag
)

python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark-conn",
    application="jobs/python/wordcountjob.py",
    dag=dag
)

print_DataFrame = SparkSubmitOperator(
    task_id="print_DataFrame",
    conn_id="spark-conn",
    application="jobs/python/dataframe.py",
    dag=dag
)

end = PythonOperator(
    task_id = "end", 
    python_callable = lambda : print("Jobs Ended"),
    dag= dag
)

start >> python_job >> print_DataFrame >> end