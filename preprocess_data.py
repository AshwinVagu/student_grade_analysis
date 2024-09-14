# preprocess_data.py
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def preprocess_student_data(df):
    # One-hot encoding for categorical variables
    df = pd.get_dummies(df, columns=['school', 'sex'], drop_first=True)

    # Normalization using MinMaxScaler
    scaler = MinMaxScaler()
    df[['age', 'studytime', 'failures', 'absences', 'G1', 'G2']] = scaler.fit_transform(df[['age', 'studytime', 'failures', 'absences', 'G1', 'G2']])

    return df
