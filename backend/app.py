from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from analysis import analyze_financial_data
from utils import allowed_file, check_missing_columns, ensure_upload_folder_exists, validate_data
from database import save_analysis_results, fetch_analysis_results, init_db

# Initialize Flask app
app = Flask(__name__)

# Set up configurations
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
app.secret_key = "your_secret_key"  # You can change this to a more secure key

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Ensure the upload folder exists
ensure_upload_folder_exists(app.config['UPLOAD_FOLDER'])

# User authentication (using Flask-Login)
from auth import auth
app.register_blueprint(auth)

# Initialize the database
@app.before_first_request
def initialize():
    """ Initialize the database before the first request """
    init_db()

# Route for the home page (landing page)
@app.route("/", methods=["GET"])
@login_required
def index():
    """ Renders the home page """
    return render_template("index.html")

# Route for uploading a file
@app.route("/upload", methods=["POST"])
@login_required
def upload_file():
    """ Handles file upload, data validation, and analysis """
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file extension
    if not allowed_file(file.filename, app.config['ALLOWED_EXTENSIONS']):
        return jsonify({'error': 'Invalid file format. Only CSV is allowed'}), 400

    # Save the uploaded file securely
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Load the data into a pandas DataFrame
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        return jsonify({'error': f"Error reading file: {str(e)}"}), 400

    # Check if required columns are missing
    missing_cols = check_missing_columns(df, ['Revenue', 'Expenses'])
    if missing_cols:
        return jsonify({'error': f'Missing columns: {", ".join(missing_cols)}'}), 400

    # Perform financial analysis and machine learning predictions
    analysis_results = analyze_financial_data(df)

    # Save the analysis results to the database
    save_analysis_results(analysis_results)

    # Render results page with analysis and insights
    return render_template("results.html", tables=df.to_html(classes='table table-bordered'),
                           analysis=analysis_results)

# Route for downloading the analysis results (example: Excel export)
@app.route('/download/<filename>', methods=['GET'])
@login_required
def download_file(filename):
    """ Allows the user to download a saved file (e.g., Excel export) """
    try:
        return redirect(url_for('static', filename=f'uploads/{filename}'))
    except Exception as e:
        return jsonify({'error': f"Error during download: {str(e)}"}), 500

# Route for viewing past analysis results
@app.route("/history", methods=["GET"])
@login_required
def view_history():
    """ Display historical analysis results """
    results = fetch_analysis_results(limit=10)  # Fetch the most recent 10 results
    return render_template("history.html", results=results)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
