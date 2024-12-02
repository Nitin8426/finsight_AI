from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

# User model class
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Simulated in-memory user database
users = {
    'admin': User(
        id=1,
        username='admin',
        password=generate_password_hash('password', method='sha256')
    )
}

@login_manager.user_loader
def load_user(user_id):
    """
    Callback to reload the user object from the user ID stored in the session.
    """
    for user in users.values():
        if str(user.id) == str(user_id):
            return user
    return None

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login. Display login form on GET and process credentials on POST.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Retrieve the user from the simulated database
        user = next((u for u in users.values() if u.username == username), None)

        if user and check_password_hash(user.password, password):
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
    Log the current user out and redirect to the login page.
    """
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration. Display registration form on GET and create new user on POST.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check for username uniqueness
        if username in (u.username for u in users.values()):
            flash('Username already exists', category='error')
            return redirect(url_for('auth.register'))

        # Validate password and confirmation
        if password != confirm_password:
            flash('Passwords do not match', category='error')
            return redirect(url_for('auth.register'))

        # Add the new user to the simulated database
        new_user_id = max(u.id for u in users.values()) + 1
        users[username] = User(
            id=new_user_id,
            username=username,
            password=generate_password_hash(password, method='sha256')
        )
        flash('Registration successful. Please log in.', category='success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
