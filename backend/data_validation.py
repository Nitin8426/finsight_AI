import pandas as pd

def validate_data(filepath, required_columns=None):
    """
    Validates the data in a CSV file to ensure required columns are present and the data is clean.
    
    Parameters:
        filepath (str): The path to the CSV file to validate.
        required_columns (list): List of required column names. Defaults to ['Revenue', 'Expenses'].
    
    Returns:
        tuple:
            - is_valid (bool): Indicates whether the data is valid.
            - errors (list): A list of validation errors, or an empty list if the data is valid.
    """
    if required_columns is None:
        required_columns = ['Revenue', 'Expenses']
    
    errors = []

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)

        # Check for missing columns
        for col in required_columns:
            if col not in df.columns:
                errors.append(f"Missing required column: '{col}'")

        # Check for null or missing values
        if df.isnull().values.any():
            errors.append("The data contains null or missing values. Please clean your data.")

        # Check for duplicate rows
        if df.duplicated().any():
            errors.append("The data contains duplicate rows. Please remove duplicates.")

        # Check for non-numeric values in numeric columns
        for col in required_columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                errors.append(f"The column '{col}' contains non-numeric values. Ensure all values are numeric.")

    except pd.errors.EmptyDataError:
        errors.append("The file is empty. Please upload a valid CSV file.")
    except pd.errors.ParserError as e:
        errors.append(f"Error parsing the file. Ensure the file is a valid CSV format. Details: {str(e)}")
    except Exception as e:
        errors.append(f"Unexpected error during validation: {str(e)}")

    # Return validation result and errors
    return len(errors) == 0, errors
