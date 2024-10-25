from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# Main Routes ############################################################################################
@main.route('/')
def index():
    site_title = 'Admin Pannel'
    author = 'Gabriel Calheiros'
    description = 'Admin Pannel'
    
    return render_template('index.html', site_title=site_title, author=author, description=description)