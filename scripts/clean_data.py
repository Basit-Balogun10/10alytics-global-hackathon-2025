import pandas as pd
import numpy as np
import os

def load_data(filepath):
    """
    Load data from a CSV or Excel file.
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Please use CSV or Excel.")

def clean_data(df):
    """
    Perform basic data cleaning.
    """
    # 1. Handle missing values (Example: Fill with median for numeric, mode for categorical)
    # This is a placeholder logic, customize based on specific dataset needs
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].median())
    
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    # 2. Remove duplicates
    df = df.drop_duplicates()
    
    return df

def save_data(df, output_path):
    """
    Save the processed data.
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    # input_file = "../data/raw/your_dataset.csv"
    # output_file = "../data/processed/cleaned_dataset.csv"
    
    # if os.path.exists(input_file):
    #     df = load_data(input_file)
    #     cleaned_df = clean_data(df)
    #     save_data(cleaned_df, output_file)
    # else:
    #     print("Input file not found. Please check the path.")
    pass
