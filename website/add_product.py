from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
import os
from werkzeug.utils import secure_filename
from . import forsale, db
from .models import Product  # Importing Product model

add_product = Blueprint('add_product', __name__)

UPLOAD_FOLDER = 'C:/Users/Anthony/Desktop/auth_update/website/static/uploads'  # Update this with the path to your upload folder
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@add_product.route('/AddProduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')

        if not (name and description and price):
            flash("Error: All fields are required.", category='error')
            return redirect(request.url)

        # Try accessing the file directly
        try:
            image = request.files['image']
        except KeyError:
            flash("Error: No file part in the request.", category='error')
            return redirect(request.url)

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)

            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)

            product = Product(
                image="/static/uploads/" + filename,
                name=name,
                description=description,
                price=price
            )

            # Add the product to the database
            db.session.add(product)
            db.session.commit()

            return redirect(url_for('views.home'))
        else:
            flash("Error: Invalid file format. Allowed formats are png, jpg, jpeg, gif", category='error')
            return redirect(request.url)

    return render_template('addproduct.html', user=current_user)

@add_product.route('/DeleteProduct/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    if product:
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('views.home'))
    else:
        return "Product not found", 404
