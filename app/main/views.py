from flask import render_template, jsonify, request, redirect, url_for, flash, session

from . import main
# import pyrebase
import firebase
from dotenv import load_dotenv
import os
load_dotenv()


config = {
    'apiKey': os.getenv("APIKEY"),
    'authDomain': os.getenv("AUTHDOMAIN"),
    'databaseURL': os.getenv("DATABASEURL"),
    'projectId': os.getenv("PROJECTID"),
    'storageBucket': os.getenv("STORAGEBUCKET"),
    'messagingSenderId': os.getenv("MESSAGINGSENDERID"),
    'appId': os.getenv("APPID"),
    'measurementId': os.getenv("MEASUREMENTID")
}

firebase = firebase.Firebase(config)
auth = firebase.auth()
db = firebase.database()


@main.route('/')
def index():
    return render_template('index.html')


# route pricing
@main.route('/pricing')
def pricing():
    return render_template('pricing.html')


# route product
@main.route('/projects')
def projects():
    return render_template('projects.html')


# route products
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


# route contacts
@main.route('/contacts')
def contacts():
    return render_template('contacts.html')


# route login
@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        try:
            auth.sign_in_with_email_and_password(email, password)
            session['user_email'] = email
            return redirect(url_for('main.index'))

        except Exception as e:
            print(e)
            return render_template('login.html', error=e)

    return render_template('index.html')


# route signup
@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print("signup POST")
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            new_user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(new_user['idToken'])
            data = {
                "email": request.form.get('email'),
                "password": request.form.get('password'),
                "phone": request.form.get('phone'),
            }

            db.child("users").push(data, new_user['idToken'])
            return render_template('login.html')
        except Exception as e:
            print(e)
            return render_template('signup.html', error=e)
    return render_template('signup.html')


# route logout
@main.route('/logout')
def logout():
    session.clear()
    print('logout')

    return redirect(url_for('main.index'))


# route tymwork
@main.route('/tymwork')
def tymwork():
    return render_template('tymwork.html')


# route phancong
@main.route('/phancong')
def phancong():
    return render_template('phancong.html')
