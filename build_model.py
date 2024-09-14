# build_model.py
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

def build_ann_model(input_shape):
    # Step 1: Initialize model
    model = Sequential()

    # Step 2: Add layers
    model.add(Dense(64, input_dim=input_shape, activation='relu'))  # Input layer
    model.add(Dense(32, activation='relu'))  # Hidden layer
    model.add(Dense(1, activation='linear'))  # Output layer (predict G3)

    # Step 3: Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    
    return model

def train_model(model, X_train, y_train, X_test, y_test):
    # Train the model
    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))
    
    return model, history
