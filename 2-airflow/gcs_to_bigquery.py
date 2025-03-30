from airflow import DAG
from airflow.utils.dates import datetime
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import timedelta

# DAG默认参数
default_args = {
    'owner': 'eliza',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# 定义DAG
with DAG(
    'gcs_to_bigquery',
    default_args=default_args,
    description='Load CSV from GCS to BigQuery',
    schedule='@daily',  # 更新为新版参数
    start_date=datetime(2025, 3, 29),  # 更新为新版日期函数
    catchup=False,
) as dag:

    # 将CSV从GCS加载到BigQuery
    load_music_dataset = GCSToBigQueryOperator(
        task_id='load_music_dataset',
        bucket='dbt-learn-452007-terra-bucket',
        source_objects=['music_dataset.csv'],
        destination_project_dataset_table='demo_dataset.music_table',
        schema_fields=[
            {'name': 'Song', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'Artist', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'Streams', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Daily_Streams', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Genre', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'Release_Year', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Peak_Position', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Weeks_on_Chart', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Lyrics_Sentiment', 'type': 'FLOAT', 'mode': 'NULLABLE'},
            {'name': 'TikTok_Virality', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'Danceability', 'type': 'FLOAT', 'mode': 'NULLABLE'},
            {'name': 'Acousticness', 'type': 'FLOAT', 'mode': 'NULLABLE'},
            {'name': 'Energy', 'type': 'FLOAT', 'mode': 'NULLABLE'},
        ],
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE',
        gcp_conn_id='google_cloud_default'  # 统一连接参数
    )