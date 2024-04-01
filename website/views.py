from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db, forsale
from .models import Product

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    products = Product.query.all()
    return render_template('home.html', user=current_user, products=products)

@views.route('/About', methods=['GET', 'POST'])
def about():
    return render_template('about.html', user=current_user)

@views.route('/Cart', methods=['GET', 'POST'])
@login_required
def cart():
    return render_template('cart.html', user=current_user)

@views.route('/Account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('acct_details.html', user=current_user)

@views.route('/ContactUs', methods=['GET', 'POST'])
@login_required
def contact():
    return render_template('contact.html', user=current_user)