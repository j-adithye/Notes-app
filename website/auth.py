from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password',category='error')
        else:
            flash('email not exist', category='error')
            
    return render_template("login.html", user = current_user)


@auth.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password1')
        
        user = User.query.filter_by(email=email).first()

        if len(email)<4:
            flash("email len 4+", category='error')
        elif user:
            flash("Email already in use")
        else:
            #add user to db
            new_user = User(email = email, first_name=first_name, last_name = last_name,password = generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash("Account Created", category='success')

            return redirect(url_for('views.home'))

    return render_template("signup.html", user= current_users)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))