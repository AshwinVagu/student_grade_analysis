# upload_predictions.py
from snowflake_connection import connect_to_snowflake, close_connection

def upload_predictions_to_snowflake(predictions, student_ids):
    conn = connect_to_snowflake()
    cursor = conn.cursor()

    # Create a new table for predictions if it doesn't exist
    cursor.execute("""
    CREATE OR REPLACE TABLE student_predictions (
        student_id INT,
        predicted_grade FLOAT
    )
    """)

    # Insert predictions
    for student_id, prediction in zip(student_ids, predictions):
        cursor.execute(f"INSERT INTO student_predictions (student_id, predicted_grade) VALUES ({student_id}, {prediction})")

    conn.commit()
    print("Predictions uploaded to Snowflake.")
    
    close_connection(conn, cursor)
