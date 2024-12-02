import os
import pandas as pd

print("utils.py loaded successfully!")
def check_missing_columns(df, required_columns):
    """
    Check for missing columns in the uploaded DataFrame.
    
    Parameters:
        df (pandas.DataFrame): The uploaded financial data as a DataFrame.
        required_columns (list): A list of required column names.
    
    Returns:
        list: A list of missing columns. Empty if all required columns are present.
    """
    if not isinstance(required_columns, list):
        raise ValueError("The required_columns parameter must be a list.")
    missing_cols = [col for col in required_columns if col not in df.columns]
    return missing_cols


def ensure_upload_folder_exists(folder_path):
    """
    Ensure the upload folder exists, creating it if necessary.
    
    Parameters:
        folder_path (str): Path to the upload folder.
    """
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Upload folder created: {folder_path}")
    except Exception as e:
        print(f"Error creating upload folder: {e}")
        raise


def allowed_file(filename, allowed_extensions):
    """
    Check if the uploaded file has an allowed extension.
    
    Parameters:
        filename (str): The name of the uploaded file.
        allowed_extensions (set): A set of allowed file extensions (e.g., {'csv'}).
    
    Returns:
        bool: True if the file is allowed, False otherwise.
    """
    if not isinstance(allowed_extensions, set):
        raise ValueError("The allowed_extensions parameter must be a set.")
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def clean_numeric_columns(df, numeric_columns):
    """
    Clean and ensure specified columns are numeric, replacing non-numeric values with NaN.
    
    Parameters:
        df (pandas.DataFrame): The uploaded financial data as a DataFrame.
        numeric_columns (list): A list of column names that must contain numeric values.
    
    Returns:
        pandas.DataFrame: The cleaned DataFrame with numeric columns.
    """
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def validate_data(df, required_columns):
    """
    Validate the DataFrame to ensure all required columns are present 
    and contain valid data.

    Parameters:
        df (pandas.DataFrame): The uploaded data as a DataFrame.
        required_columns (list): A list of required column names.

    Returns:
        bool: True if the data is valid, raises an exception otherwise.
    """
    missing_columns = check_missing_columns(df, required_columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Add additional validations as needed
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Example: Check for NaN values in required columns
    for col in required_columns:
        if df[col].isnull().any():
            raise ValueError(f"Column {col} contains missing values.")
    
    return True

def validate_file_size(filepath, max_size_mb=5):
    """
    Validate the file size of the uploaded file.
    
    Parameters:
        filepath (str): Path to the uploaded file.
        max_size_mb (int): Maximum allowed file size in MB.
    
    Returns:
        bool: True if the file size is within the allowed limit, False otherwise.
    """
    try:
        file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
        return file_size_mb <= max_size_mb
    except Exception as e:
        print(f"Error checking file size: {e}")
        return False
