import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def analyze_financial_data(df):
    """
    Perform financial calculations and generate insights based on the provided financial data.
    
    Parameters:
        df (pandas.DataFrame): DataFrame containing financial data (e.g., Revenue, Expenses, Month).
    
    Returns:
        analysis_results (dict): Summary of financial metrics (e.g., total revenue, net profit).
        insights (list): List of insights and recommendations based on the analysis.
    """
    # Ensure required columns exist
    if 'Revenue' not in df.columns or 'Expenses' not in df.columns:
        raise ValueError("Missing required columns: 'Revenue' and 'Expenses'")

    # Financial calculations
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    net_profit = total_revenue - total_expenses
    profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

    # Generate insights
    insights = []
    if profit_margin < 10:
        insights.append("Profit margin is low. Consider reducing operational expenses or increasing revenue.")
    else:
        insights.append("Profit margin is healthy. Keep maintaining the current strategies.")

    if total_expenses > total_revenue:
        insights.append("Warning: Expenses exceed revenue. Consider cost-cutting measures.")
    else:
        insights.append("Revenue exceeds expenses. Keep optimizing your financials for growth.")

    # Optional: Predict future revenue if 'Month' column exists
    if 'Month' in df.columns:
        future_revenue_prediction, ml_insights = predict_future_revenue(df)
        insights.extend(ml_insights)
        insights.append(f"Projected revenue for next month: ${future_revenue_prediction:,.2f}")

    # Compile results
    analysis_results = {
        'Total Revenue': total_revenue,
        'Total Expenses': total_expenses,
        'Net Profit': net_profit,
        'Profit Margin (%)': profit_margin
    }

    return analysis_results, insights


def predict_future_revenue(df, next_month=13, model_type='linear'):
    """
    Use a machine learning model to predict future revenue based on historical data.
    
    Parameters:
        df (pandas.DataFrame): DataFrame containing 'Month' and 'Revenue' columns.
        next_month (int): The next month for which revenue is to be predicted.
        model_type (str): The type of ML model to use ('linear' or 'random_forest').
    
    Returns:
        future_revenue_prediction (float): Predicted revenue for the next month.
        ml_insights (list): Insights based on the model's performance and predictions.
    """
    # Ensure required columns exist
    if 'Month' not in df.columns or 'Revenue' not in df.columns:
        raise ValueError("Missing required columns: 'Month' and 'Revenue'")

    # Prepare the data
    X = df[['Month']]  # Feature: Month
    y = df['Revenue']  # Target: Revenue
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select and train the model
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'random_forest':
        model = RandomForestRegressor(random_state=42)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    # Predict future revenue
    future_revenue_prediction = model.predict([[next_month]])[0]

    # Generate insights
    ml_insights = [
        f"Machine learning model used: {model_type.capitalize()}",
        f"Model RMSE: {rmse:.2f} (lower is better).",
        "The model uses historical revenue data to predict future revenue."
    ]

    return future_revenue_prediction, ml_insights
