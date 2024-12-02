import pandas as pd
import os

def export_to_excel(data, filename='analysis_results.xlsx', sheet_name='Analysis Results'):
    """
    Export analysis results to an Excel file.
    
    Parameters:
        data (list of dict or dict): The analysis results to export.
            - If list of dict, each dictionary represents a row of data.
            - If dict, keys represent column names, and values are lists representing columns.
        filename (str): The name of the Excel file to create.
        sheet_name (str): The name of the sheet where data will be stored.
    
    Returns:
        str: The path to the generated Excel file.
    """
    try:
        # Convert the data into a DataFrame
        if isinstance(data, dict):
            df = pd.DataFrame(data)
        elif isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            raise ValueError("Data must be a dictionary or a list of dictionaries.")

        # Create the uploads directory if it doesn't exist
        uploads_dir = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        # Construct the full path for the Excel file
        file_path = os.path.join(uploads_dir, filename)

        # Write the DataFrame to an Excel file
        df.to_excel(file_path, index=False, sheet_name=sheet_name)
        print(f"Data successfully exported to {file_path}")

        return file_path
    except Exception as e:
        print(f"Error exporting data to Excel: {str(e)}")
        return None
