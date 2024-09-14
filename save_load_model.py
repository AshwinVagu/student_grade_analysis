# save_load_model.py
from tensorflow.python.keras.models import load_model

def save_model(model, file_path="student_performance_model.h5"):
    # Save the model to a local file
    model.save(file_path)
    print(f"Model saved to {file_path}")

def load_model_from_file(file_path="student_performance_model.h5"):
    # Load the model from a file
    model = load_model(file_path)
    print(f"Model loaded from {file_path}")
    return model
