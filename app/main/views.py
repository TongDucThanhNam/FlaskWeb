import jinja2
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/services')
def services():
    return render_template('services.html')


# route project
@main.route('/projects')
def project():
    return render_template('projects.html')


# route pricing
@main.route('/pricing')
def pricing():
    return render_template('pricing.html')


# route product
@main.route('/product')
def product():
    return render_template('products.html')

#route products
@main.route('/project_init')
def project_init():
    return render_template('project_init.html')


# route shopping cart
@main.route('/shopping_cart')
def shopping_cart():
    return render_template('shopping-cart.html')


# route Team
@main.route('/team')
def team():
    return render_template('team.html')


# route testimonials
@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


# route contacts
@main.route('/contacts')
def contacts():
    return render_template('contacts.html')


# route login
@main.route('/login')
def login():
    return render_template('login.html')


# route signup
@main.route('/signup')
def signup():
    return render_template('signup.html')


