from flask import Blueprint, render_template, request, flash  #help us organize our files

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
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
            flash('all is good', category='success')
   
    return render_template("signup.html")