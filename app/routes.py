from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from flask import current_app
from app.models import Category, Subcategory, Feed  # Adjust path if necessary

from app import db  # Importe db conforme a estrutura do seu projeto

# Importing from fetch_scripts.py
from app.fetch_scripts import parse_opml_to_df, fetch_rss_feed

from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

# Directory to store uploaded OPML files temporarily
UPLOAD_FOLDER = './tmp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Main Routes ############################################################################################
@main.route('/')
def index():
    site_title = 'Admin Pannel'
    author = 'Gabriel Calheiros'
    description = 'Admin Pannel'
    
    return render_template('index.html', site_title=site_title, author=author, description=description)


# Import OPML ############################################################################################

@main.route('/import_opml', methods=['GET', 'POST'])
def import_opml():
    if request.method == 'POST':
        # Check if file is in the request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # Check if the file has a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            # Secure the filename and save it
            filename = secure_filename(file.filename)
            file_path = os.path.join('./tmp/', filename)
            file.save(file_path)

            # Parse OPML and convert to DataFrame
            feeds_df = parse_opml_to_df(file_path)

            # Insert feeds into the database
            for _, row in feeds_df.iterrows():
                category_name = row['Category']
                subcategory_name = row['Subcategory']
                feed_name = row['Feed']
                html_url = row['htmlUrl']
                xml_url = row['xmlUrl']

                # Check if the category exists, else create it
                category = Category.query.filter_by(category_name=category_name).first()
                if not category:
                    category = Category(category_name=category_name)
                    db.session.add(category)
                    db.session.flush()  # Flush to get id_category for use in feed

                # Check if the subcategory exists, else create it
                subcategory = Subcategory.query.filter_by(name_subcategory=subcategory_name).first()
                if not subcategory:
                    subcategory = Subcategory(name_subcategory=subcategory_name, id_view=1)  # Adjust id_view as needed
                    db.session.add(subcategory)
                    db.session.flush()  # Flush to get id_subcategory for use in feed

                # Create the feed, linking it to category and subcategory IDs
                feed = Feed(
                    feed_name=feed_name,
                    html_url=html_url,
                    xml_url=xml_url,
                    id_category=category.id_category,
                    id_subcategory=subcategory.id_subcategory,
                    feed_icon=""  # Optional: set feed_icon if needed
                )
                db.session.add(feed)

            # Commit all changes to the database
            db.session.commit()
            flash('OPML file imported successfully')
            return redirect(url_for('main.index'))

    return render_template('import_opml.html')
