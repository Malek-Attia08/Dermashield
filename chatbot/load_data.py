# chatbot/load_data.py
import pandas as pd

def load_medical_data():
    # Path to the dataset (adjust this based on where you stored it)
    dataset_path = r"D:\chatbot\Medical_Intelligence_Dataset.csv"

    df = pd.read_csv(dataset_path)
    return df[['input', 'output']]  # Extract relevant columns
