from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, template_folder='templates/main')

@main_bp.route('/main')
def main():
    return render_template('main.html')

