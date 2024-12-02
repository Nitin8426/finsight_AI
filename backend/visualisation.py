import matplotlib.pyplot as plt
import os

def generate_bar_chart(data, title='Financial Analysis Metrics', filename='bar_chart.png', color='skyblue'):
    """
    Generate a bar chart from the provided data and save it as an image file.
    
    Parameters:
        data (dict): Dictionary containing labels and corresponding values for the bar chart.
        title (str): The title of the chart.
        filename (str): The filename where the chart will be saved (e.g., 'bar_chart.png').
        color (str): Color of the bars in the chart.
    """
    try:
        labels = data.keys()
        values = data.values()

        # Create the bar chart
        plt.bar(labels, values, color=color)

        # Set chart title and labels
        plt.title(title)
        plt.ylabel('Value')

        # Ensure the 'static' folder exists
        static_folder = 'static'
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)

        # Save the chart as a PNG file in the 'static' folder
        file_path = os.path.join(static_folder, filename)
        plt.savefig(file_path)
        plt.close()

        print(f"Bar chart saved as {file_path}")
        return file_path
    except Exception as e:
        print(f"Error generating bar chart: {e}")
        return None

def generate_line_chart(data, title='Financial Trends', filename='line_chart.png', color='green'):
    """
    Generate a line chart from the provided data and save it as an image file.
    
    Parameters:
        data (dict): Dictionary containing labels (months, years, etc.) and corresponding values for the line chart.
        title (str): The title of the chart.
        filename (str): The filename where the chart will be saved (e.g., 'line_chart.png').
        color (str): Color of the line in the chart.
    """
    try:
        labels = list(data.keys())
        values = list(data.values())

        # Create the line chart
        plt.plot(labels, values, marker='o', color=color)

        # Set chart title and labels
        plt.title(title)
        plt.xlabel('Time Period')
        plt.ylabel('Value')

        # Ensure the 'static' folder exists
        static_folder = 'static'
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)

        # Save the chart as a PNG file in the 'static' folder
        file_path = os.path.join(static_folder, filename)
        plt.savefig(file_path)
        plt.close()

        print(f"Line chart saved as {file_path}")
        return file_path
    except Exception as e:
        print(f"Error generating line chart: {e}")
        return None

def generate_pie_chart(data, title='Financial Distribution', filename='pie_chart.png'):
    """
    Generate a pie chart from the provided data and save it as an image file.
    
    Parameters:
        data (dict): Dictionary containing labels and values for the pie chart.
        title (str): The title of the chart.
        filename (str): The filename where the chart will be saved (e.g., 'pie_chart.png').
    """
    try:
        labels = data.keys()
        values = data.values()

        # Create the pie chart
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

        # Set chart title
        plt.title(title)

        # Ensure the 'static' folder exists
        static_folder = 'static'
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)

        # Save the chart as a PNG file in the 'static' folder
        file_path = os.path.join(static_folder, filename)
        plt.savefig(file_path)
        plt.close()

        print(f"Pie chart saved as {file_path}")
        return file_path
    except Exception as e:
        print(f"Error generating pie chart: {e}")
        return None
