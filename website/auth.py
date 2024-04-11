from flask import Blueprint, render_template, request, flash, redirect, url_for  #help us organize our files
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db




auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
            else:
                flash('Incorrect Password',category='error' )
        else:
            flash('User does not exist', category='error')
        
    return render_template("login.html")
    
@auth.route('/logout')
def logout():
    return '<p>logout</p>'
    
    
@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email is too short.', category='error')
        elif len(name) < 2:
            flash('Name is too short', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 4:
            flash('The length of your password should be above 4 characters', category='error')
        else:
            #add to database
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully.', category='success')
            return redirect(url_for('views.home', name=name))
   
    return render_template("signup.html")