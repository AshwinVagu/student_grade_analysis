# main.py
from query_data import query_student_data
from preprocess_data import preprocess_student_data
from build_model import build_ann_model, train_model
from evaluate_model import evaluate_model, plot_loss
from save_load_model import save_model, load_model_from_file
from upload_predictions import upload_predictions_to_snowflake
from snowflake_connection import upload_file_to_snowflake_stage
from sklearn.model_selection import train_test_split

def main():
    # Step 1: Query data from Snowflake
    student_df = query_student_data()

    # Step 2: Preprocess the data
    processed_df = preprocess_student_data(student_df)

    # Step 3: Split the data into training and testing sets
    X = processed_df.drop(columns=['G3'])
    y = processed_df['G3']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Build the ANN model
    model = build_ann_model(X_train.shape[1])

    # Step 5: Train the model
    model, history = train_model(model, X_train, y_train, X_test, y_test)

    # Step 6: Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Step 7: Plot the training loss
    plot_loss(history)

    # Step 8: Save the trained model locally
    model_file_path = "student_performance_model.h5"
    save_model(model, model_file_path)

    # Step 9: Upload the trained model to Snowflake stage
    upload_file_to_snowflake_stage(model_file_path, "student_model_stage")

    # Step 10: Make predictions on the test data and upload them to Snowflake
    predictions = model.predict(X_test).flatten()  # Generate predictions
    student_ids = X_test.index.tolist()  # Use the DataFrame index as student IDs
    upload_predictions_to_snowflake(predictions, student_ids)

if __name__ == "__main__":
    main()
