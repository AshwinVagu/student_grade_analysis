# evaluate_model.py
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    loss, mae = model.evaluate(X_test, y_test)
    print(f'Mean Absolute Error: {mae}')
    return mae

def plot_loss(history):
    # Plot the training & validation loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper right')
    plt.show()
