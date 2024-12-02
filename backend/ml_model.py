import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def analyze_financial_data(df, model_type='random_forest'):
    """
    Perform financial analysis and predict future profits using a machine learning model.
    
    Parameters:
        df (pandas.DataFrame): Financial data with columns 'Revenue' and 'Expenses'.
        model_type (str): The type of ML model to use ('random_forest' or 'linear_regression').
    
    Returns:
        dict: A dictionary containing financial metrics and ML predictions.
    """
    # Ensure necessary columns are present
    if 'Revenue' not in df.columns or 'Expenses' not in df.columns:
        raise ValueError("Missing required columns: 'Revenue' and 'Expenses'")

    # Calculate total financial metrics
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    profit = total_revenue - total_expenses

    # Add a 'Profit' column if it does not exist
    if 'Profit' not in df.columns:
        df['Profit'] = df['Revenue'] - df['Expenses']

    # ML Model: Predict future profits
    results = train_and_predict(df, model_type)

    return {
        'Total Revenue': total_revenue,
        'Total Expenses': total_expenses,
        'Profit': profit,
        'Predictions': results['Predictions'],
        'Model Info': results['Model Info'],
        'Metrics': results['Metrics']
    }

def train_and_predict(df, model_type='random_forest'):
    """
    Train a machine learning model and make predictions.
    
    Parameters:
        df (pandas.DataFrame): Financial data with columns 'Revenue', 'Expenses', and 'Profit'.
        model_type (str): The type of ML model to use ('random_forest' or 'linear_regression').
    
    Returns:
        dict: A dictionary containing predictions and model evaluation metrics.
    """
    # Prepare features and target
    X = df[['Revenue', 'Expenses']]  # Features: Revenue, Expenses
    y = df['Profit']  # Target: Profit

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select and train the model
    if model_type == 'random_forest':
        model = RandomForestRegressor(random_state=42)
        model_name = 'Random Forest Regressor'
    elif model_type == 'linear_regression':
        model = LinearRegression()
        model_name = 'Linear Regression'
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    return {
        'Predictions': predictions.tolist(),
        'Model Info': {
            'Model Type': model_name,
            'Feature Importance': model.feature_importances_.tolist() if hasattr(model, 'feature_importances_') else None
        },
        'Metrics': {
            'Mean Squared Error (MSE)': mse,
            'R-squared (R2)': r2
        }
    }
