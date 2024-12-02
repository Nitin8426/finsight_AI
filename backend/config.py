from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

# User class for session management
class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

# In-memory user database
users = {
    "admin": User(
        id=1,
        username="admin",
        password_hash=generate_password_hash("password", method="sha256")
    )
}

@login_manager.user_loader
def load_user(user_id):
    """
    Callback to reload the user object from the user ID stored in the session.
    """
    return next((u for u in users.values() if str(u.id) == str(user_id)), None)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.
    GET: Renders the login page.
    POST: Authenticates user credentials and starts the session.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if user exists
        user = next((u for u in users.values() if u.username == username), None)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful', category='success')
            return redirect(url_for('index'))  # Redirect to the home page
        else:
            flash('Invalid username or password', category='error')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    """
    Log out the current user and redirect to the login page.
    """
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.
    GET: Renders the registration page.
    POST: Adds a new user to the in-memory database after validation.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate form inputs
        if username in (u.username for u in users.values()):
            flash('Username already exists. Please choose a different one.', category='error')
            return redirect(url_for('auth.register'))
        if password != confirm_password:
            flash('Passwords do not match.', category='error')
            return redirect(url_for('auth.register'))

        # Add the new user to the database
        new_user_id = max(u.id for u in users.values()) + 1
        users[username] = User(
            id=new_user_id,
            username=username,
            password_hash=generate_password_hash(password, method="sha256")
        )
        flash('Registration successful! You can now log in.', category='success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
