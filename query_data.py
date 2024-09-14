# query_data.py
import pandas as pd
from snowflake_connection import connect_to_snowflake, close_connection

def query_student_data():
    # Step 1: Establish connection
    conn = connect_to_snowflake()
    cursor = conn.cursor()

    # Step 2: Define query
    query = "SELECT * FROM student_performance;"
    cursor.execute(query)

    # Step 3: Fetch data and convert to DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=[col[0] for col in cursor.description])

    # Step 4: Close connection
    close_connection(conn, cursor)
    
    return df
