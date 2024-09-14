# snowflake_connection.py
import snowflake.connector
import logging


def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user='<enter_username>',
        password='<enter_password>',
        account='<enter_account>',
        warehouse='<enter_warehouse>',
        database='student_performance_db',
        schema='student_data_schema',
        role='ACCOUNTADMIN'
    )
    return conn

def close_connection(conn, cursor):
    cursor.close()
    conn.close()


def upload_file_to_snowflake_stage(file_path, stage_name):
    conn = connect_to_snowflake()
    cursor = conn.cursor()
    query = f"PUT file://{file_path} @{stage_name} AUTO_COMPRESS=TRUE"
    cursor.execute(query)
    print(f"File {file_path} uploaded to Snowflake stage: {stage_name}")
    close_connection(conn, cursor)