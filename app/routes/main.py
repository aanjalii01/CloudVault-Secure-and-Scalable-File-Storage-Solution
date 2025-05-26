from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    # You can treat index as your dashboard page
    return render_template('index.html', user=current_user)

@main.route('/dashboard')
@login_required
def user_dashboard():
    # This can be the same as index or a separate dashboard page
    return render_template('dashboard.html', user=current_user)
