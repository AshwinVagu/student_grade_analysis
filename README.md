# Student Performance Prediction Using Artificial Neural Network (ANN) and Snowflake

## Project Overview
This project implements an Artificial Neural Network (ANN) model to predict future academic performance based on student details and past grades. The system leverages **Snowflake Data Warehouse** for efficient and scalable data storage and retrieval. Input data, such as student details and past grades, are initially stored in an **AWS S3** bucket and then ingested into **Snowflake Data Warehouse**, where predictions are generated and stored.

## Features
- **ANN Model**: Predicts student performance based on past academic records.
- **Snowflake Integration**: Input data and output predictions are stored and managed within Snowflake, ensuring scalability.
- **AWS S3**: Used as a storage solution for initial data ingestion before loading into Snowflake.

## Requirements
- **Python 3.x**
- Libraries specified in `requirements.txt`

## Project Structure
. ├── data/ │ ├── input/ # Contains initial student data files ├── src/ │ ├── ann_model.py # ANN model definition and training │ ├── data_loader.py # Data ingestion logic for AWS S3 and Snowflake │ ├── predict.py # Script to generate predictions │ ├── main.py # Main script to run the project ├── requirements.txt # Required Python libraries ├── README.md # Project documentation



## Setup and Installation

1. **Clone the repository:**
   git clone <repository_url>
   cd <repository_name>

Install required dependencies: Make sure you have Python 3.x installed. Install the libraries from the requirements.txt file:

pip install -r requirements.txt

Configure AWS S3 and Snowflake credentials:
Ensure you have your AWS and Snowflake credentials properly configured for data access.
How to Run the Project

Prepare the data:
Ensure the input data (student details and grades) is available in the data/input directory or in AWS S3 for ingestion.
Run the main script: To start the student performance prediction, execute the following command:

python main.py

This will load data from AWS S3, ingest it into Snowflake, train the ANN model, and generate predictions.
Output

The model's predictions will be saved in Snowflake, where the results can be retrieved and analyzed.