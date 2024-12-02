import sqlite3

DB_NAME = "financial_analysis.db"

def init_db():
    """
    Initialize the SQLite database and create the necessary tables if they do not exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_revenue REAL,
                total_expenses REAL,
                net_profit REAL,
                profit_margin REAL,
                predictions TEXT
            )
        ''')
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        conn.close()

def save_analysis_results(results):
    """
    Save analysis results to the database.
    
    Parameters:
        results (dict): Dictionary containing analysis results with keys:
            - 'Total Revenue'
            - 'Total Expenses'
            - 'Net Profit'
            - 'Profit Margin (%)'
            - 'Predictions'
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # Insert the analysis results into the table
        c.execute('''
            INSERT INTO analysis_results (total_revenue, total_expenses, net_profit, profit_margin, predictions)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            results.get('Total Revenue', 0),
            results.get('Total Expenses', 0),
            results.get('Net Profit', 0),
            results.get('Profit Margin (%)', 0),
            results.get('Predictions', 'No predictions available')
        ))
        conn.commit()
        print("Analysis results saved successfully.")
    except sqlite3.Error as e:
        print(f"Error saving analysis results: {e}")
    finally:
        conn.close()

def fetch_analysis_results(limit=10):
    """
    Fetch the most recent analysis results from the database.
    
    Parameters:
        limit (int): The maximum number of results to fetch. Defaults to 10.
    
    Returns:
        list of dict: A list of dictionaries containing the analysis results.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # Fetch the latest results
        c.execute('''
            SELECT id, total_revenue, total_expenses, net_profit, profit_margin, predictions
            FROM analysis_results
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        rows = c.fetchall()

        # Convert rows to dictionaries
        results = [
            {
                "id": row[0],
                "Total Revenue": row[1],
                "Total Expenses": row[2],
                "Net Profit": row[3],
                "Profit Margin (%)": row[4],
                "Predictions": row[5],
            }
            for row in rows
        ]
        return results
    except sqlite3.Error as e:
        print(f"Error fetching analysis results: {e}")
        return []
    finally:
        conn.close()

if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Example usage: Save analysis results
    example_results = {
        'Total Revenue': 15000,
        'Total Expenses': 10000,
        'Net Profit': 5000,
        'Profit Margin (%)': 33.33,
        'Predictions': "Revenue expected to increase by 10% next month."
    }
    save_analysis_results(example_results)

    # Example usage: Fetch the latest results
    recent_results = fetch_analysis_results(limit=5)
    print("Recent Analysis Results:")
    for result in recent_results:
        print(result)
