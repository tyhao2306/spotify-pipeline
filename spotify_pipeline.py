from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="spotify_data_pipeline",
    default_args=default_args,
    description="Fetch and store Spotify data",
    schedule_interval="@daily",  # or change to whatever you prefer
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    fetch_recently_played = BashOperator(
        task_id="fetch_recently_played",
        bash_command="python /opt/airflow/dags/spotify_recently_played.py"
    )

    fetch_genres = BashOperator(
        task_id="fetch_genres",
        bash_command="python /opt/airflow/dags/get_genre.py"
    )

    fetch_recently_played >> fetch_genres
